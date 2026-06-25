import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'GIS Setup Bot online as {bot.user.name}!')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_gis(ctx):
    guild = ctx.guild
    await ctx.send("🚨 **Initializing GREEDY INTEL SERVICE (GIS) Server Setup...** This will take a few moments.")

    try:
        # ==========================================
        # 1. ROLE GENERATION
        # ==========================================
        # Colors used to differentiate branches visually
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

        # Executive Command
        dir_intel = await guild.create_role(name="Director of Intelligence", permissions=discord.Permissions(administrator=True), color=c_exec)
        dep_dir = await guild.create_role(name="Deputy Director", permissions=discord.Permissions(administrator=True), color=c_exec)
        exec_oversight = await guild.create_role(name="Executive Oversight Authority", permissions=discord.Permissions(administrator=True), color=c_exec)

        # Senior Command
        chief_intel = await guild.create_role(name="Chief of Intelligence", color=c_senior)
        chief_ia = await guild.create_role(name="Chief of Internal Affairs", color=c_senior)

        # Division Command
        intel_cmd = await guild.create_role(name="Intelligence Commander", color=c_div)
        ia_cmd = await guild.create_role(name="Internal Affairs Commander", color=c_div)

        # Intelligence Division
        sr_intel_analyst = await guild.create_role(name="Senior Intelligence Analyst", color=c_intel)
        intel_analyst = await guild.create_role(name="Intelligence Analyst", color=c_intel)

        # Internal Affairs Division
        sr_ia_investigator = await guild.create_role(name="Senior IA Investigator", color=c_ia)
        ia_investigator = await guild.create_role(name="IA Investigator", color=c_ia)

        # Administrative Support Roles
        recruitment = await guild.create_role(name="Recruitment Team", color=c_admin)
        training = await guild.create_role(name="Training Staff", color=c_admin)
        records = await guild.create_role(name="Records Management", color=c_admin)
        compliance = await guild.create_role(name="Compliance Officer", color=c_admin)
        comms_off = await guild.create_role(name="Communications Officer", color=c_admin)
        ops_coord = await guild.create_role(name="Operations Coordinator", color=c_admin)

        # Clearance Levels
        cl_1 = await guild.create_role(name="Clearance Level I", color=c_clear)
        cl_2 = await guild.create_role(name="Clearance Level II", color=c_clear)
        cl_3 = await guild.create_role(name="Clearance Level III", color=c_clear)
        cl_4 = await guild.create_role(name="Clearance Level IV", color=c_clear)
        cl_5 = await guild.create_role(name="Clearance Level V", color=c_clear)

        # Status Roles
        verified = await guild.create_role(name="Verified Personnel", color=c_status)
        probationary = await guild.create_role(name="Probationary Personnel", color=c_status)
        under_investigation = await guild.create_role(name="Under Investigation", color=c_status)
        active_review = await guild.create_role(name="Active Review", color=c_status)
        suspended = await guild.create_role(name="Suspended Access", color=c_status)
        # FIXED: Using RGB (1,1,1) for black instead of the non-existent .black() attribute
        blacklisted = await guild.create_role(name="Blacklisted", color=discord.Color.from_rgb(1, 1, 1))

        # Operations Roles
        active_ops = await guild.create_role(name="Active Operations", color=c_ops)
        intel_tf = await guild.create_role(name="Intelligence Task Force", color=c_ops)
        case_lead = await guild.create_role(name="Case Lead", color=c_ops)
        field_ops = await guild.create_role(name="Field Operations", color=c_ops)
        threat_team = await guild.create_role(name="Threat Assessment Team", color=c_ops)

        # Service & Recognition & Executive Awards
        awards = [
            "30 Day Service Ribbon", "90 Day Service Ribbon", "180 Day Service Ribbon", "1 Year Service Ribbon",
            "Distinguished Service Award", "Intelligence Excellence Award", "Investigative Excellence Award",
            "Leadership Excellence Award", "Community Service Award", "Director's Commendation",
            "Executive Achievement Award", "Meritorious Service Award", "Operational Excellence Award"
        ]
        for award in awards:
            await guild.create_role(name=award, color=c_award)

        # Honorary Roles
        honorary = ["Veteran Personnel", "Senior Operative", "Elite Analyst", "Intelligence Specialist", "Honorary Member", "Founding Member"]
        for hon in honorary:
            await guild.create_role(name=hon, color=c_honor)

        # Disciplinary Markers
        markers = ["Verbal Warning", "Written Warning", "Strike I", "Strike II", "Strike III", "Final Review"]
        for marker in markers:
            await guild.create_role(name=marker, color=c_warn)

        # Helper permission combinations
        exec_group = [dir_intel, dep_dir, exec_oversight]
        senior_cmd_group = exec_group + [chief_intel, chief_ia]
        all_command = senior_cmd_group + [intel_cmd, ia_cmd]
        intel_division = [intel_cmd, sr_intel_analyst, intel_analyst]
        ia_division = [ia_cmd, sr_ia_investigator, ia_investigator]

        # ==========================================
        # 2. CATEGORY & CHANNEL GENERATION WITH PERMISSIONS
        # ==========================================

        # --- CORE CATEGORY ---
        cat_core = await guild.create_category("📌 CORE")
        
        # Welcome
        ow_welcome = {
            guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False),
            verified: discord.PermissionOverwrite(view_channel=True, send_messages=False),
            recruitment: discord.PermissionOverwrite(view_channel=True, manage_messages=True),
        }
        await guild.create_text_channel("gis│welcome", category=cat_core, overwrites=ow_welcome)

        # Directives
        ow_directives = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        for r in senior_cmd_group: ow_directives[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await guild.create_text_channel("gis│directives", category=cat_core, overwrites=ow_directives)

        # Announcements
        ow_announcements = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), comms_off: discord.PermissionOverwrite(send_messages=True, view_channel=True)}
        for r in exec_group: ow_announcements[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await guild.create_text_channel("gis│announcements", category=cat_core, overwrites=ow_announcements)

        # Regulations
        ow_regs = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), compliance: discord.PermissionOverwrite(send_messages=True, view_channel=True)}
        for r in exec_group: ow_regs[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await guild.create_text_channel("gis│regulations", category=cat_core, overwrites=ow_regs)


        # --- COMMAND CATEGORY ---
        cat_cmd = await guild.create_category("🚨 COMMAND")
        
        # High Command
        ow_hc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_hc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await guild.create_text_channel("gis│high-command", category=cat_cmd, overwrites=ow_hc)

        # Command Briefing
        ow_cb = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in senior_cmd_group: ow_cb[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await guild.create_text_channel("gis│command-briefing", category=cat_cmd, overwrites=ow_cb)

        # Oversight
        ow_os = {guild.default_role: discord.PermissionOverwrite(view_channel=False), chief_ia: discord.PermissionOverwrite(view_channel=True), ia_cmd: discord.PermissionOverwrite(view_channel=True), compliance: discord.PermissionOverwrite(view_channel=True)}
        for r in exec_group: ow_os[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│oversight", category=cat_cmd, overwrites=ow_os)


        # --- OPERATIONS & INTEL CATEGORY ---
        cat_ops_intel = await guild.create_category("⚡ OPERATIONS & INTEL")
        
        # Operations
        ow_ops = {guild.default_role: discord.PermissionOverwrite(view_channel=False), ops_coord: discord.PermissionOverwrite(view_channel=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True)}
        for r in senior_cmd_group + [intel_cmd, ia_cmd] + intel_division: ow_ops[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│operations", category=cat_ops_intel, overwrites=ow_ops)

        # Case Files
        ow_cf = {guild.default_role: discord.PermissionOverwrite(view_channel=False), records: discord.PermissionOverwrite(view_channel=True), case_lead: discord.PermissionOverwrite(view_channel=True)}
        for r in intel_division + ia_division: ow_cf[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│case-files", category=cat_ops_intel, overwrites=ow_cf)

        # Threat Levels
        ow_tl = {guild.default_role: discord.PermissionOverwrite(view_channel=False), threat_team: discord.PermissionOverwrite(view_channel=True), cl_3: discord.PermissionOverwrite(view_channel=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True)}
        for r in intel_division: ow_tl[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│threat-levels", category=cat_ops_intel, overwrites=ow_tl)

        # Intel Reports
        ow_ir = {guild.default_role: discord.PermissionOverwrite(view_channel=False), intel_tf: discord.PermissionOverwrite(view_channel=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True)}
        for r in intel_division: ow_ir[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│intel-reports", category=cat_ops_intel, overwrites=ow_ir)


        # --- INTERNAL CONTROL CATEGORY ---
        cat_ic = await guild.create_category("🛡️ INTERNAL CONTROL")
        
        # Internal Affairs
        ow_ia = {guild.default_role: discord.PermissionOverwrite(view_channel=False), chief_ia: discord.PermissionOverwrite(view_channel=True)}
        for r in ia_division: ow_ia[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│internal-affairs", category=cat_ic, overwrites=ow_ia)

        # Disciplinary
        ow_disc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in ia_division + exec_group: ow_disc[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│disciplinary", category=cat_ic, overwrites=ow_disc)

        # Compliance
        ow_comp = {guild.default_role: discord.PermissionOverwrite(view_channel=False), compliance: discord.PermissionOverwrite(view_channel=True)}
        for r in ia_division + senior_cmd_group: ow_comp[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│compliance", category=cat_ic, overwrites=ow_comp)


        # --- COMMUNICATION CATEGORY ---
        cat_comm = await guild.create_category("💬 COMMUNICATION")
        
        # General Chat
        ow_gen = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True)}
        await guild.create_text_channel("gis│general", category=cat_comm, overwrites=ow_gen)

        # Secure Comms
        ow_sc = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            verified: discord.PermissionOverwrite(view_channel=True),
            cl_2: discord.PermissionOverwrite(view_channel=True),
            under_investigation: discord.PermissionOverwrite(view_channel=False)  # Explicit lockout
        }
        for r in all_command: ow_sc[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│secure-comms", category=cat_comm, overwrites=ow_sc)

        # Briefing Room VC
        ow_vc = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True)}
        await guild.create_voice_channel("gis│briefing-room", category=cat_comm, overwrites=ow_vc)


        # --- SUPPORT CATEGORY ---
        cat_support = await guild.create_category("🤝 SUPPORT")
        
        # Applications
        ow_app = {guild.default_role: discord.PermissionOverwrite(view_channel=True), recruitment: discord.PermissionOverwrite(view_channel=True)}
        for r in exec_group: ow_app[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│applications", category=cat_support, overwrites=ow_app)

        # Tickets
        ow_tix = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in all_command: ow_tix[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│tickets", category=cat_support, overwrites=ow_tix)

        # Appeals
        ow_ap = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True)}
        for r in ia_division + all_command: ow_ap[r] = discord.PermissionOverwrite(view_channel=True)
        await guild.create_text_channel("gis│appeals", category=cat_support, overwrites=ow_ap)

        await ctx.send("✅ **GIS Server Structure successfully established!** All roles generated and access overrides mapped out.")

    except Exception as e:
        await ctx.send(f"❌ **An error occurred during creation:** {e}")

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
