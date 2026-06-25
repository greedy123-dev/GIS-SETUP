import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'GIS Master Infrastructure Bot online as {bot.user.name}!')

# ==========================================
# MODULE 1: !setup_roles
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_roles(ctx):
    guild = ctx.guild
    await ctx.send("🚨 **MODULE 1/3: WIPING & ARCHITECTING FULL SECURITY AND HONOR ROLES...** Please wait.")

    # Clean out old roles below the bot's rank safely
    for role in list(guild.roles):
        if not role.is_default() and role < guild.me.top_role:
            try:
                await role.delete()
                await asyncio.sleep(0.2)
            except Exception:
                pass

    try:
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
        
        # Leadership & Command Tiers
        await guild.create_role(name="Director of Intelligence", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Deputy Director", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Executive Oversight Authority", permissions=exec_perms, color=c_exec, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Chief of Intelligence", color=c_senior, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Chief of Internal Affairs", color=c_senior, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Intelligence Commander", color=c_div, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Internal Affairs Commander", color=c_div, mentionable=False)
        await asyncio.sleep(0.2)

        # Tactical Divisions & Logistics
        await guild.create_role(name="Senior Intelligence Analyst", color=c_intel, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Intelligence Analyst", color=c_intel, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Senior IA Investigator", color=c_ia, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="IA Investigator", color=c_ia, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Recruitment Team", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Training Staff", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Records Management", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Compliance Officer", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Communications Officer", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)
        await guild.create_role(name="Operations Coordinator", color=c_admin, mentionable=False)
        await asyncio.sleep(0.2)

        # Clearances, Access, and Safety Lists
        for lvl in ["I", "II", "III", "IV", "V"]:
            await guild.create_role(name=f"Clearance Level {lvl}", color=c_clear, mentionable=False)
            await asyncio.sleep(0.2)

        for status in ["Verified Personnel", "Probationary Personnel", "Under Investigation", "Active Review", "Suspended Access"]:
            await guild.create_role(name=status, color=c_status, mentionable=False)
            await asyncio.sleep(0.2)
        await guild.create_role(name="Blacklisted", color=discord.Color.from_rgb(1, 1, 1), mentionable=False)
        await asyncio.sleep(0.2)

        # Active Frontline Combat Units
        for tf in ["Active Operations", "Intelligence Task Force", "Case Lead", "Field Operations", "Threat Assessment Team"]:
            await guild.create_role(name=tf, color=c_ops, mentionable=False)
            await asyncio.sleep(0.2)

        # Service Ribbons & Commendations
        awards = ["30 Day Service Ribbon", "90 Day Service Ribbon", "180 Day Service Ribbon", "1 Year Service Ribbon", "Distinguished Service Award", "Intelligence Excellence Award", "Investigative Excellence Award", "Leadership Excellence Award", "Community Service Award", "Director's Commendation", "Executive Achievement Award", "Meritorious Service Award", "Operational Excellence Award"]
        for award in awards:
            await guild.create_role(name=award, color=c_award, mentionable=False)
            await asyncio.sleep(0.2)

        # Legendary & Honorary Statuses
        honorary = ["Veteran Personnel", "Senior Operative", "Elite Analyst", "Intelligence Specialist", "Honorary Member", "Founding Member"]
        for hon in honorary:
            await guild.create_role(name=hon, color=c_honor, mentionable=False)
            await asyncio.sleep(0.2)

        # System Tracking & Infractions
        markers = ["Verbal Warning", "Written Warning", "Strike I", "Strike II", "Strike III", "Final Review"]
        for marker in markers:
            await guild.create_role(name=marker, color=c_warn, mentionable=False)
            await asyncio.sleep(0.2)

        # Enforce baseline locked server state
        await guild.default_role.edit(permissions=discord.Permissions(view_channel=False, send_messages=False, mention_everyone=False))
        await ctx.send("✅ **Roles successfully deployed!** Move to the next module by typing: `!setup_channels`")
    except Exception as e:
        print(f"Error building database tiers: {e}")

# ==========================================
# MODULE 2: !setup_channels
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_channels(ctx):
    guild = ctx.guild
    trigger_channel = ctx.channel
    await ctx.send("🚨 **MODULE 2/3: DEPLOYING MASSIVE SYSTEM CATEGORIES & SECURITY OVERRIDES...** Please wait.")

    # Sweep old layout channels while holding your active execution room safe
    for channel in list(guild.channels):
        if channel != trigger_channel:
            try:
                await channel.delete()
                await asyncio.sleep(0.3)
            except Exception:
                pass

    # Map security positions directly from internal server list
    roles = {r.name: r for r in guild.roles}
    def fetch_group(names):
        return [roles[n] for n in names if n in roles]

    exec_group = fetch_group(["Director of Intelligence", "Deputy Director", "Executive Oversight Authority"])
    senior_cmd_group = exec_group + fetch_group(["Chief of Intelligence", "Chief of Internal Affairs"])
    all_command = senior_cmd_group + fetch_group(["Intelligence Commander", "Internal Affairs Commander"])
    intel_division = fetch_group(["Intelligence Commander", "Senior Intelligence Analyst", "Intelligence Analyst"])
    ia_division = fetch_group(["Internal Affairs Commander", "Senior IA Investigator", "IA Investigator"])
    
    verified = roles.get("Verified Personnel")
    recruitment = roles.get("Recruitment Team")
    blacklisted = roles.get("Blacklisted")
    comms_off = roles.get("Communications Officer")
    ops_coord = roles.get("Operations Coordinator")
    under_investigation = roles.get("Under Investigation")
    cl_4 = roles.get("Clearance Level IV")
    cl_5 = roles.get("Clearance Level V")
    intel_tf = roles.get("Intelligence Task Force")
    chief_ia = roles.get("Chief of Internal Affairs")

    async def create_secure_channel(name, category, overwrites, is_voice=False):
        if is_voice:
            await guild.create_voice_channel(name, category=category, overwrites=overwrites)
            await asyncio.sleep(0.5)
            return
        await guild.create_text_channel(name, category=category, overwrites=overwrites)
        await asyncio.sleep(0.5)

    try:
        # --- CORE ---
        cat_core = await guild.create_category("📌 CORE")
        await asyncio.sleep(0.5)
        
        ow_welcome = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        if verified: ow_welcome[verified] = discord.PermissionOverwrite(view_channel=True, send_messages=False)
        if recruitment: ow_welcome[recruitment] = discord.PermissionOverwrite(view_channel=True, manage_messages=True)
        if blacklisted: ow_welcome[blacklisted] = discord.PermissionOverwrite(view_channel=False)
        await create_secure_channel("gis│welcome", cat_core, ow_welcome)

        ow_directives = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        if blacklisted: ow_directives[blacklisted] = discord.PermissionOverwrite(view_channel=False)
        for r in senior_cmd_group: ow_directives[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│directives", cat_core, ow_directives)

        ow_announcements = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        if comms_off: ow_announcements[comms_off] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        if blacklisted: ow_announcements[blacklisted] = discord.PermissionOverwrite(view_channel=False)
        for r in exec_group: ow_announcements[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_secure_channel("gis│announcements", cat_core, ow_announcements)

        # --- COMMAND ---
        cat_cmd = await guild.create_category("🚨 COMMAND")
        await asyncio.sleep(0.5)
        
        ow_hc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_group: ow_hc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│high-command", cat_cmd, ow_hc)

        # --- OPERATIONS & INTEL ---
        cat_ops_intel = await guild.create_category("⚡ OPERATIONS & INTEL")
        await asyncio.sleep(0.5)
        
        ow_ops = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if ops_coord: ow_ops[ops_coord] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        if cl_4: ow_ops[cl_4] = discord.PermissionOverwrite(view_channel=True)
        if cl_5: ow_ops[cl_5] = discord.PermissionOverwrite(view_channel=True)
        if under_investigation: ow_ops[under_investigation] = discord.PermissionOverwrite(view_channel=False)
        for r in all_command + intel_division: ow_ops[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│operations", cat_ops_intel, ow_ops)

        ow_ir = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if intel_tf: ow_ir[intel_tf] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        if cl_4: ow_ir[cl_4] = discord.PermissionOverwrite(view_channel=True)
        if cl_5: ow_ir[cl_5] = discord.PermissionOverwrite(view_channel=True)
        for r in intel_division: ow_ir[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│intel-reports", cat_ops_intel, ow_ir)

        # --- INTERNAL CONTROL ---
        cat_ic = await guild.create_category("🛡️ INTERNAL CONTROL")
        await asyncio.sleep(0.5)
        
        ow_ia = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if chief_ia: ow_ia[chief_ia] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        for r in ia_division: ow_ia[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│internal-affairs", cat_ic, ow_ia)

        # --- COMMUNICATION ---
        cat_comm = await guild.create_category("💬 COMMUNICATION")
        await asyncio.sleep(0.5)
        
        ow_gen = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if verified: ow_gen[verified] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_secure_channel("gis│general", cat_comm, ow_gen)

        ow_vc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if verified: ow_vc[verified] = discord.PermissionOverwrite(view_channel=True, connect=True, speak=True)
        await create_secure_channel("gis│briefing-room", cat_comm, ow_vc, is_voice=True)

        await ctx.send("✅ **Structural matrix ready!** Trigger final automation block by typing: `!setup_webhooks`")
    except Exception as e:
        print(f"Error building channels: {e}")

# ==========================================
# MODULE 3: !setup_webhooks (REAL WEBHOOKS + REAL EMBEDS)
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_webhooks(ctx):
    guild = ctx.guild
    await ctx.send("🔌 **MODULE 3/3: DEPLOYING WEBHOOK ROUTERS & FIRING ADVANCED DIAGNOSTIC EMBEDS...** Please wait.")
    await asyncio.sleep(1)

    # Dictionary configuring avatars and distinct look-and-feel for each real channel webhook
    webhook_configs = {
        "gis│welcome": {
            "name": "GIS Gateway Terminal",
            "avatar": "https://i.imgur.com/vH97Z9P.png",
            "title": "🛰️ SYSTEM SECURITY TERMINAL",
            "desc": "Welcome to the GIS Central Command. Your clearance levels and identities are currently indexing against database records.\n\n🔒 **STATUS:** UNVERIFIED until processed.",
            "color": 0x8b0000
        },
        "gis│directives": {
            "name": "GIS Directive Node",
            "avatar": "https://i.imgur.com/u5v0r4O.png",
            "title": "📜 EXECUTIVE STRATEGIC DIRECTIVES",
            "desc": "This interface logs mandate frameworks and intelligence system structural orders directly from High Command.",
            "color": 0xcd5c5c
        },
        "gis│announcements": {
            "name": "GIS Broadcasting Net",
            "avatar": "https://i.imgur.com/qR8Y8b7.png",
            "title": "📢 GLOBAL COMMAND BROADCAST",
            "desc": "Real-time updates, active theatre shifts, and operational statuses are dispatched across this encryption band.",
            "color": 0xdaa520
        },
        "gis│high-command": {
            "name": "GIS HQ Relay",
            "avatar": "https://i.imgur.com/fK7tS2k.png",
            "title": "🚨 HIGH COMMAND QUANTUM ENVELOPE",
            "desc": "Secure communication terminal optimized for High Command elements and Executive Oversight. Interception is classified as a severe security threat.",
            "color": 0x1e90ff
        },
        "gis│operations": {
            "name": "GIS Tactical Uplink",
            "avatar": "https://i.imgur.com/O1H2w7v.png",
            "title": "⚡ ACTIVE STRATEGIC OPERATIONS",
            "desc": "Live field operations tracker and tactical movement board. Authorized personnel must update mission tracking files sequentially.",
            "color": 0xff4500
        },
        "gis│intel-reports": {
            "name": "GIS Analysis Core",
            "avatar": "https://i.imgur.com/Y3UuXWv.png",
            "title": "📁 INTELLIGENCE ARCHIVE LOGS",
            "desc": "Central repository for gathered intelligence data, active threat models, and field analysis files.",
            "color": 0x00ced1
        },
        "gis│internal-affairs": {
            "name": "GIS Integrity Matrix",
            "avatar": "https://i.imgur.com/M6X8w7v.png",
            "title": "🛡️ INTERNAL AFFAIRS COMPLIANCE LOG",
            "desc": "Monitoring interface for active reviews, field compliance logs, and internal integrity operations.",
            "color": 0x4b0082
        }
    }

    success = 0
    for channel in guild.text_channels:
        if channel.name in webhook_configs:
            cfg = webhook_configs[channel.name]
            try:
                # 1. Create the actual system Webhook
                webhook = await channel.create_webhook(name=cfg["name"])
                await asyncio.sleep(0.6)
                
                # 2. Build a high-end Discord Embed message payload
                embed = discord.Embed(
                    title=cfg["title"],
                    description=cfg["desc"],
                    color=discord.Color(cfg["color"])
                )
                embed.set_footer(text="GLOBAL INTELLIGENCE SYSTEM • AUTOMATION COMPLETED", icon_url=cfg["avatar"])
                
                # 3. Fire the real webhook using custom avatars and details
                await webhook.send(embed=embed, username=cfg["name"], avatar_url=cfg["avatar"])
                success += 1
                await asyncio.sleep(0.6)
            except Exception as e:
                print(f"Error handling webhook logic inside channel '{channel.name}': {e}")

    await ctx.send(f"🏆 **System deployment fully finalized!** Real webhooks with custom graphic avatars and secure embed configurations deployed across {success} primary text lines.")
    
    # Dissolve the initialization text room cleanly
    try:
        await ctx.channel.delete()
    except Exception:
        pass

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
