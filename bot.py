import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'GIS Paced Setup Bot online as {bot.user.name}!')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_gis(ctx):
    guild = ctx.guild
    trigger_channel = ctx.channel
    
    await trigger_channel.send("🚨 **INITIALIZING PACED PURGE & BUILD...** This version pauses to prevent Discord rate limits. Please wait.")

    # ==========================================
    # 1. PACED PURGE (Channels & Roles)
    # ==========================================
    # Clean out channels with a slight safety pause
    for channel in list(guild.channels):
        if channel != trigger_channel:
            try:
                await channel.delete()
                await asyncio.sleep(0.5)  # Pause to avoid rate limits
            except Exception:
                pass

    # Clean out old roles below the bot's rank
    for role in list(guild.roles):
        if not role.is_default() and role < guild.me.top_role:
            try:
                await role.delete()
                await asyncio.sleep(0.5)  # Pause to avoid rate limits
            except Exception:
                pass

    try:
        # ==========================================
        # 2. ROLE ARCHITECTURE (Unpingable by default)
        # ==========================================
        c_exec = discord.Color.from_rgb(139, 0, 0)      
        c_senior = discord.Color.from_rgb(205, 92, 92)  
        c_div = discord.Color.from_rgb(218, 165, 32)   
        c_intel = discord.Color.from_rgb(30, 144, 255)  
        c_ia = discord.Color.from_rgb(75, 0, 130)       
        c_admin = discord.Color.from_rgb(46, 139, 87)   
        c_clear = discord.Color.from_rgb(192, 192, 192) 
        c_status = discord.Color.from_rgb(128, 128, 128)
        c_ops = discord.Color.from_rgb(255, 69, 0)      
        c_award = discord.Color.from_rgb(255, 215, 0)     
        c_honor = discord.Color.from_rgb(0, 206, 209)   
        c_warn = discord.Color.from_rgb(255, 140, 0)    

        exec_perms = discord.Permissions(administrator=True, mention_everyone=True)
        dir_intel = await guild.create_role(name="Director of Intelligence", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.3)
        dep_dir = await guild.create_role(name="Deputy Director", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.3)
        exec_oversight = await guild.create_role(name="Executive Oversight Authority", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.3)

        chief_intel = await guild.create_role(name="Chief of Intelligence", color=c_senior, mentionable=False)
        await asyncio.sleep(0.3)
        chief_ia = await guild.create_role(name="Chief of Internal Affairs", color=c_senior, mentionable=False)
        await asyncio.sleep(0.3)
        intel_cmd = await guild.create_role(name="Intelligence Commander", color=c_div, mentionable=False)
        await asyncio.sleep(0.3)
        ia_cmd = await guild.create_role(name="Internal Affairs Commander", color=c_div, mentionable=False)
        await asyncio.sleep(0.3)

        sr_intel_analyst = await guild.create_role(name="Senior Intelligence Analyst", color=c_intel, mentionable=False)
        await asyncio.sleep(0.3)
        intel_analyst = await guild.create_role(name="Intelligence Analyst", color=c_intel, mentionable=False)
        await asyncio.sleep(0.3)
        sr_ia_investigator = await guild.create_role(name="Senior IA Investigator", color=c_ia, mentionable=False)
        await asyncio.sleep(0.3)
        ia_investigator = await guild.create_role(name="IA Investigator", color=c_ia, mentionable=False)
        await asyncio.sleep(0.3)

        recruitment = await guild.create_role(name="Recruitment Team", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)
        training = await guild.create_role(name="Training Staff", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)
        records = await guild.create_role(name="Records Management", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)
        compliance = await guild.create_role(name="Compliance Officer", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)
        comms_off = await guild.create_role(name="Communications Officer", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)
        ops_coord = await guild.create_role(name="Operations Coordinator", color=c_admin, mentionable=False)
        await asyncio.sleep(0.3)

        cl_1 = await guild.create_role(name="Clearance Level I", color=c_clear, mentionable=False)
        await asyncio.sleep(0.3)
        cl_2 = await guild.create_role(name="Clearance Level II", color=c_clear, mentionable=False)
        await asyncio.sleep(0.3)
        cl_3 = await guild.create_role(name="Clearance Level III", color=c_clear, mentionable=False)
        await asyncio.sleep(0.3)
        cl_4 = await guild.create_role(name="Clearance Level IV", color=c_clear, mentionable=False)
        await asyncio.sleep(0.3)
        cl_5 = await guild.create_role(name="Clearance Level V", color=c_clear, mentionable=False)
        await asyncio.sleep(0.3)

        verified = await guild.create_role(name="Verified Personnel", color=c_status, mentionable=False)
        await asyncio.sleep(0.3)
        probationary = await guild.create_role(name="Probationary Personnel", color=c_status, mentionable=False)
        await asyncio.sleep(0.3)
        under_investigation = await guild.create_role(name="Under Investigation", color=c_status, mentionable=False)
        await asyncio.sleep(0.3)
        active_review = await guild.create_role(name="Active Review", color=c_status, mentionable=False)
        await asyncio.sleep(0.3)
        suspended = await guild.create_role(name="Suspended Access", color=c_status, mentionable=False)
        await asyncio.sleep(0.3)
        blacklisted = await guild.create_role(name="Blacklisted", color=discord.Color.from_rgb(1, 1, 1), mentionable=False)
        await asyncio.sleep(0.3)

        active_ops = await guild.create_role(name="Active Operations", color=c_ops, mentionable=False)
        await asyncio.sleep(0.3)
        intel_tf = await guild.create_role(name="Intelligence Task Force", color=c_ops, mentionable=False)
        await asyncio.sleep(0.3)
        case_lead = await guild.create_role(name="Case Lead", color=c_ops, mentionable=False)
        await asyncio.sleep(0.3)
        field_ops = await guild.create_role(name="Field Operations", color=c_ops, mentionable=False)
        await asyncio.sleep(0.3)
        threat_team = await guild.create_role(name="Threat Assessment Team", color=c_ops, mentionable=False)
        await asyncio.sleep(0.3)

        # Mappings
        exec_group = [dir_intel, dep_dir, exec_oversight]
        senior_cmd_group = exec_group + [chief_intel, chief_ia]
        all_command = senior_cmd_group + [intel_cmd, ia_cmd]
        intel_division = [intel_cmd, sr_intel_analyst, intel_analyst]
        ia_division = [ia_cmd, sr_ia_investigator, ia_investigator]

        # Lock down @everyone basic permissions
        await guild.default_role.edit(permissions=discord.Permissions(view_channel=False, send_messages=False, mention_everyone=False))
        await asyncio.sleep(1)

        # Helper channel generation build functions with built-in breaks
        async def create_secure_channel(name, category, overwrites, need_webhook=False, is_voice=False):
            if is_voice:
                ch = await guild.create_voice_channel(name, category=category, overwrites=overwrites)
                await asyncio.sleep(1)
                return ch
            
            ch = await guild.create_text_channel(name, category=category, overwrites=overwrites)
            await asyncio.sleep(1)
            await ch.send("placeholder")
            await asyncio.sleep(0.5)
            if need_webhook:
                await ch.create_webhook(name=f"{name.replace('│', '-')}-Automation")
                await asyncio.sleep(1)
            return ch

        # ==========================================
        # 3. PACED SYSTEM BUILDING
        # ==========================================

        # --- CORE ---
        cat_core = await guild.create_category("📌 CORE")
        await asyncio.sleep(1)
        
        ow_welcome = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=False), recruitment: discord.PermissionOverwrite(view_channel=True, manage_messages=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        await create_secure_channel("gis│welcome", cat_core, ow_welcome)

        ow_directives = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in senior_cmd_group: ow_directives[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│directives", cat_core, ow_directives)

        ow_announcements = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), comms_off: discord.PermissionOverwrite(send_messages=True, view_channel=True), blacklisted: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_announcements[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│announcements", cat_core, ow_announcements, need_webhook=True)


        # --- COMMAND ---
        cat_cmd = await guild.create_category("🚨 COMMAND")
        await asyncio.sleep(1)
        
        ow_hc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_hc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│high-command", cat_cmd, ow_hc, need_webhook=True)


        # --- OPERATIONS & INTEL ---
        cat_ops_intel = await guild.create_category("⚡ OPERATIONS & INTEL")
        await asyncio.sleep(1)
        
        ow_ops = {guild.default_role: discord.PermissionOverwrite(view_channel=False), ops_coord: discord.PermissionOverwrite(view_channel=True, send_messages=True), cl_4: discord.PermissionOverwrite(view_channel=True), cl_5: discord.PermissionOverwrite(view_channel=True), under_investigation: discord.PermissionOverwrite(view_channel=False)}
        for r in all_command + intel_division: ow_ops[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│operations", cat_ops_intel, ow_ops)

        ow_ir = {guild.default_role: discord.PermissionOverwrite(view_channel=False), intel_tf: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        for r in intel_division: ow_ir[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│intel-reports", cat_ops_intel, ow_ir, need_webhook=True)


        # --- INTERNAL CONTROL ---
        cat_ic = await guild.create_category("🛡️ INTERNAL CONTROL")
        await asyncio.sleep(1)
        
        ow_ia = {guild.default_role: discord.PermissionOverwrite(view_channel=False), chief_ia: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        for r in ia_division: ow_ia[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│internal-affairs", cat_ic, ow_ia, need_webhook=True)


        # --- COMMUNICATION ---
        cat_comm = await guild.create_category("💬 COMMUNICATION")
        await asyncio.sleep(1)
        
        ow_gen = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        await create_secure_channel("gis│general", cat_comm, ow_gen)

        ow_vc = {guild.default_role: discord.PermissionOverwrite(view_channel=False), verified: discord.PermissionOverwrite(view_channel=True, connect=True, speak=True)}
        await create_secure_channel("gis│briefing-room", cat_comm, ow_vc, is_voice=True)

        # Clear the setup message channel safely once done
        try:
            await trigger_channel.delete()
        except Exception:
            pass

    except Exception as e:
        print(f"Error handling sequential deployment process: {e}")

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
