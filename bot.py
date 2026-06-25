import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'GIS Ultimate Setup Bot online as {bot.user.name}!')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_gis(ctx):
    guild = ctx.guild
    trigger_channel = ctx.channel
    
    await trigger_channel.send("🚨 **NUCLEAR PURGE & ULTRALOCKDOWN INITIALIZED... GO GO GO!**")

    # ==========================================
    # 1. IMMEDIATE FULL PURGE (Channels & Roles)
    # ==========================================
    # Delete channels except the one running the command
    for channel in list(guild.channels):
        if channel != trigger_channel:
            try:
                await channel.delete()
            except Exception:
                pass

    # Delete all custom roles beneath the bot's rank
    for role in list(guild.roles):
        if not role.is_default() and role < guild.me.top_role:
            try:
                await role.delete()
            except Exception:
                pass

    try:
        # ==========================================
        # 2. ROLE ARCHITECTURE (mentionable=False / Anti-Raid)
        # ==========================================
        c_exec = discord.Color.from_rgb(139, 0, 0)      # Dark Red
        c_senior = discord.Color.from_rgb(205, 92, 92)  # Light Red/Coral
        c_div = discord.Color.from_rgb(218, 165, 32)   # Goldenrod
        c_intel = discord.Color.from_rgb(30, 144, 255)  # Dodger Blue
        c_ia = discord.Color.from_rgb(75, 0, 130)       # Indigo
        c_admin = discord.Color.from_rgb(46, 139, 87)   # Sea Green
        c_clear = discord.Color.from_rgb(192, 192, 192) # Silver
        c_status = discord.Color.from_rgb(128, 128, 128)# Gray
        c_ops = discord.Color.from_rgb(255, 69, 0)      # Orange Red
        c_award = discord.Color.from_rgb(255, 215, 0)     # Gold
        c_honor = discord.Color.from_rgb(0, 206, 209)   # Dark Turquoise
        c_warn = discord.Color.from_rgb(255, 140, 0)    # Dark Orange

        # High Commands bypass ping defenses natively using mention_everyone permissions
        exec_perms = discord.Permissions(administrator=True, mention_everyone=True)
        dir_intel = await guild.create_role(name="Director of Intelligence", permissions=exec_perms, color=c_exec, mentionable=False)
        dep_dir = await guild.create_role(name="Deputy Director", permissions=exec_perms, color=c_exec, mentionable=False)
        exec_oversight = await guild.create_role(name="Executive Oversight Authority", permissions=exec_perms, color=c_exec, mentionable=False)

        # Command Staff
        chief_intel = await guild.create_role(name="Chief of Intelligence", color=c_senior, mentionable=False)
        chief_ia = await guild.create_role(name="Chief of Internal Affairs", color=c_senior, mentionable=False)
        intel_cmd = await guild.create_role(name="Intelligence Commander", color=c_div, mentionable=False)
        ia_cmd = await guild.create_role(name="Internal Affairs Commander", color=c_div, mentionable=False)

        # Field Operatives
        sr_intel_analyst = await guild.create_role(name="Senior Intelligence Analyst", color=c_intel, mentionable=False)
        intel_analyst = await guild.create_role(name="Intelligence Analyst", color=c_intel, mentionable=False)
        sr_ia_investigator = await guild.create_role(name="Senior IA Investigator", color=c_ia, mentionable=False)
        ia_investigator = await guild.create_role(name="IA Investigator", color=c_ia, mentionable=False)

        # Administration & Ops Support
        recruitment = await guild.create_role(name="Recruitment Team", color=c_admin, mentionable=False)
        training = await guild.create_role(name="Training Staff", color=c_admin, mentionable=False)
        records = await guild.create_role(name="Records Management", color=c_admin, mentionable=False)
        compliance = await guild.create_role(name="Compliance Officer", color=c_admin, mentionable=False)
        comms_off = await guild.create_role(name="Communications Officer", color=c_admin, mentionable=False)
        ops_coord = await guild.create_role(name="Operations Coordinator", color=c_admin, mentionable=False)

        # Security Levels
        cl_1 = await guild.create_role(name="Clearance Level I", color=c_clear, mentionable=False)
        cl_2 = await guild.create_role(name="Clearance Level II", color=c_clear, mentionable=False)
        cl_3 = await guild.create_role(name="Clearance Level III", color=c_clear, mentionable=False)
        cl_4 = await guild.create_role(name="Clearance Level IV", color=c_clear, mentionable=False)
        cl_5 = await guild.create_role(name="Clearance Level V", color=c_clear, mentionable=False)

        # Verification States
        verified = await guild.create_role(name="Verified Personnel", color=c_status, mentionable=False)
        probationary = await guild.create_role(name="Probationary Personnel", color=c_status, mentionable=False)
        under_investigation = await guild.create_role(name="Under Investigation", color=c_status, mentionable=False)
        active_review = await guild.create_role(name="Active Review", color=c_status, mentionable=False)
        suspended = await guild.create_role(name="Suspended Access", color=c_status, mentionable=False)
        blacklisted = await guild.create_role(name="Blacklisted", color=discord.Color.from_rgb(1, 1, 1), mentionable=False)

        # Operational Taskforces
        active_ops = await guild.create_role(name="Active Operations", color=c_ops, mentionable=False)
        intel_tf = await guild.create_role(name="Intelligence Task Force", color=c_ops, mentionable=False)
        case_lead = await guild.create_role(name="Case Lead", color=c_ops, mentionable=False)
        field_ops = await guild.create_role(name="Field Operations", color=c_ops, mentionable=False)
        threat_team = await guild.create_role(name="Threat Assessment Team", color=c_ops, mentionable=False)

        # Service Awards
        awards = ["30 Day Service Ribbon", "90 Day Service Ribbon", "180 Day Service Ribbon", "1 Year Service Ribbon", "Distinguished Service Award", "Intelligence Excellence Award", "Investigative Excellence Award", "Leadership Excellence Award", "Community Service Award", "Director's Commendation", "Executive Achievement Award", "Meritorious Service Award", "Operational Excellence Award"]
        for award in awards: await guild.create_role(name=award, color=c_award, mentionable=False)

        # Honorary Ranks
        honorary = ["Veteran Personnel", "Senior Operative", "Elite Analyst", "Intelligence Specialist", "Honorary Member", "Founding Member"]
        for hon in honorary: await guild.create_role(name=hon, color=c_honor, mentionable=False)

        # Disciplinary States
        markers = ["Verbal Warning", "Written Warning", "Strike I", "Strike II", "Strike III", "Final Review"]
        for marker in markers: await guild.create_role(name=marker, color=c_warn, mentionable=False)

        # Group Mapping Definitions
        exec_group = [dir_intel, dep_dir, exec_oversight]
        senior_cmd_group = exec_group + [chief_intel, chief_ia]
        all_command = senior_cmd_group + [intel_cmd, ia_cmd]
        intel_division = [intel_cmd, sr_intel_analyst, intel_analyst]
        ia_division = [ia_cmd, sr_ia_investigator, ia_investigator]

        # Stripping generic user roles of permissions to block basic bot exploits/raids
        await guild.default_role.edit(permissions=discord.Permissions(view_channel=False, send_messages=False, mention_everyone=False, create_public_threads=False, create_private_threads=False))

        # Core Channel Generation Helper Logic
        async def create_secure_channel(name, category, overwrites, need_webhook=False, is_voice=False):
            if is_voice:
                return await guild.create_voice_channel(name, category=category, overwrites=overwrites)
            
            ch = await guild.create_text_channel(name, category=category, overwrites=overwrites)
            await ch.send("placeholder")
            if need_webhook:
                await ch.create_webhook(name=f"{name.replace('│', '-')}-Automation")
            return ch

        # ==========================================
        # 3. HIGH-SPEED CATEGORY & SYSTEM SETUP
        # ==========================================

        # --- BRANCH I: CORE SYSTEMS ---
        cat_core = await guild.create_category("📌 CORE")
        
        ow_welcome = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=False), recruitment: discord.PermissionOverwrite(view_channel=True, manage_messages=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        await create_secure_channel("gis│welcome", cat_core, ow_welcome)

        ow_directives = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in senior_cmd_group: ow_directives[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│directives", cat_core, ow_directives)

        ow_announcements = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), comms_off: discord.PermissionOverwrite(send_messages=True, view_channel=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_announcements[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│announcements", cat_core, ow_announcements, need_webhook=True)

        ow_regs = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), compliance: discord.PermissionOverwrite(send_messages=True, view_channel=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_regs[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│regulations", cat_core, ow_regs)


        # --- BRANCH II: HIGH COMMAND (MAX ENCRYPTION) ---
        cat_cmd = await guild.create_category("🚨 COMMAND")
        
        ow_hc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_hc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│high-command", cat_cmd, ow_hc, need_webhook=True)

        ow_cb = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in senior_cmd_group: ow_cb[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│command-briefing", cat_cmd, ow_cb, need_webhook=True)

        ow_os = {guild.default_role: discord.PermissionOverwrite(view_channel=False), chief_ia: discord.PermissionOverwrite(view_channel=True), ia_cmd: discord.PermissionOverwrite(view_channel=True), compliance: discord.PermissionOverwrite(view_channel=True)}
        for r in exec_group: ow_os[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│oversight", cat_cmd, ow_os)


        # --- BRANCH III: OPERATIONS & INTEEL ---
        cat_ops_intel = await guild.create_category("⚡ OPERATIONS & INTEL")
        
        ow_ops = {guild.default_role: discord.PermissionOverwrite(view_channel=False), ops_coord: discord.PermissionOverwrite(view_channel=True, send_messages=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True), under_investigation: discord.PermissionOverwrite(view_channel=False), suspended: discord.PermissionOverwrite(view_channel=False)}
        for r in all_command + intel_division: ow_ops[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│operations", cat_ops_intel, ow_ops)

        ow_cf = {guild.default_role: discord.PermissionOverwrite(view_channel=False), records: discord.PermissionOverwrite(view_channel=True, send_messages=True), case_lead: discord.PermissionOverwrite(view_channel=True, send_messages=True), under_investigation: discord.PermissionOverwrite(view_channel=False), suspended: discord.PermissionOverwrite(view_channel=False)}
        for r in intel_division + ia_division: ow_cf[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│case-files", cat_ops_intel, ow_cf, need_webhook=True)

        ow_tl = {guild.default_role: discord.PermissionOverwrite(view_channel=False), threat_team: discord.PermissionOverwrite(view_channel=True, send_messages=True), cl_3: discord.PermissionOverwrite(view_channel=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True)}
        for r in intel_division: ow_tl[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│threat-levels", cat_ops_intel, ow_tl)

        ow_ir = {guild.default_role: discord.PermissionOverwrite(view_channel=False), intel_tf: discord.PermissionOverwrite(view_channel=True, send_messages=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True)}
        for r in intel_division: ow_ir[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│intel-reports", cat_ops_intel, ow_ir, need_webhook=True)


        # --- BRANCH IV: INTERNAL AFFAIRS (COUNTER-INTELLIGENCE) ---
        cat_ic = await guild.create_category("🛡️ INTERNAL CONTROL")
        
        ow_ia = {guild.default_role: discord.PermissionOverwrite(view_channel=False), chief_ia: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        for r in ia_division: ow_ia[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│internal-affairs", cat_ic, ow_ia, need_webhook=True)

        ow_disc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in ia_division + exec_group: ow_disc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│disciplinary", cat_ic, ow_disc, need_webhook=True)

        ow_comp = {guild.default_role: discord.PermissionOverwrite(view_channel=False), compliance: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        for r in ia_division + senior_cmd_group: ow_comp[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│compliance", cat_ic, ow_comp)


        # --- BRANCH V: COMM LINE DATA STREAMS ---
        cat_comm = await guild.create_category("💬 COMMUNICATION")
        
        ow_gen = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=True), under_investigation: discord.PermissionOverwrite(view_channel=False), suspended: discord.PermissionOverwrite(view_channel=False)}
        await create_secure_channel("gis│general", cat_comm, ow_gen)

        ow_sc = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=True), cl_2: discord.PermissionOverwrite(view_channel=True), under_investigation: discord.PermissionOverwrite(view_channel=False), suspended: discord.PermissionOverwrite(view_channel=False)}
        for r in all_command: ow_sc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│secure-comms", cat_comm, ow_sc)

        ow_vc = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, connect=True, speak=True), under_investigation: discord.PermissionOverwrite(view_channel=False), suspended: discord.PermissionOverwrite(view_channel=False)}
        await create_secure_channel("gis│briefing-room", cat_comm, ow_vc, is_voice=True)


        # --- BRANCH VI: FRONT DESK & INTAKE ---
        cat_support = await guild.create_category("🤝 SUPPORT")
        
        ow_app = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=True), recruitment: discord.PermissionOverwrite(view_channel=True, send_messages=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_app[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│applications", cat_support, ow_app)

        ow_tix = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in all_command: ow_tix[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│tickets", cat_support, ow_tix, need_webhook=True)

        ow_ap = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=True), suspended: discord.PermissionOverwrite(view_channel=True, send_messages=True), under_investigation: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        for r in ia_division + all_command: ow_ap[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│appeals", cat_support, ow_ap)

        # Final purge transaction complete - drop trigger communication line safely
        try:
            await trigger_channel.delete()
        except Exception:
            pass

    except Exception as e:
        print(f"Error executing absolute secure layout deployment: {e}")

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
