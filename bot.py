import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'GIS Modular Bot online as {bot.user.name}!')

# ==========================================
# COMMAND 1: !setup_roles
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_roles(ctx):
    guild = ctx.guild
    await ctx.send("🔨 **Step 1/3:** Wiping old roles and deploying unpingable GIS security tiers...")

    # Paced Role Purge
    for role in list(guild.roles):
        if not role.is_default() and role < guild.me.top_role:
            try:
                await role.delete()
                await asyncio.sleep(0.2)
            except Exception:
                continue

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

        exec_perms = discord.Permissions(administrator=True, mention_everyone=True)
        
        roles_to_create = [
            ("Director of Intelligence", exec_perms, c_exec),
            ("Deputy Director", exec_perms, c_exec),
            ("Executive Oversight Authority", exec_perms, c_exec),
            ("Chief of Intelligence", None, c_senior),
            ("Chief of Internal Affairs", None, c_senior),
            ("Intelligence Commander", None, c_div),
            ("Internal Affairs Commander", None, c_div),
            ("Senior Intelligence Analyst", None, c_intel),
            ("Intelligence Analyst", None, c_intel),
            ("Senior IA Investigator", None, c_ia),
            ("IA Investigator", None, c_ia),
            ("Recruitment Team", None, c_admin),
            ("Training Staff", None, c_admin),
            ("Records Management", None, c_admin),
            ("Compliance Officer", None, c_admin),
            ("Operations Coordinator", None, c_admin),
            ("Clearance Level I", None, c_clear),
            ("Clearance Level II", None, c_clear),
            ("Clearance Level III", None, c_clear),
            ("Clearance Level IV", None, c_clear),
            ("Clearance Level V", None, c_clear),
            ("Verified Personnel", None, c_status),
            ("Probationary Personnel", None, c_status),
            ("Under Investigation", None, c_status),
            ("Suspended Access", None, c_status),
            ("Blacklisted", None, discord.Color.from_rgb(1, 1, 1)),
            ("Active Operations", None, c_ops),
            ("Intelligence Task Force", None, c_ops)
        ]

        for name, perms, color in roles_to_create:
            await guild.create_role(name=name, permissions=perms or discord.Permissions.none(), color=color, mentionable=False)
            await asyncio.sleep(0.2)
        
        await guild.default_role.edit(permissions=discord.Permissions(view_channel=False, send_messages=False, mention_everyone=False))
        await ctx.send("✅ **Roles established successfully!** Move on to Step 2 by typing: `!setup_channels`")

    except Exception as e:
        await ctx.send(f"❌ Error during roles step: {e}")


# ==========================================
# COMMAND 2: !setup_channels
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_channels(ctx):
    guild = ctx.guild
    await ctx.send("📂 **Step 2/3:** Purging channels and building fully configured security categories...")

    # Safe clear of old channels (except current execution line)
    for channel in list(guild.channels):
        if channel.id != ctx.channel.id:
            try:
                await channel.delete()
                await asyncio.sleep(0.2)
            except Exception:
                continue

    # Map created roles dynamically from the guild roster
    roles = {r.name: r for r in guild.roles}
    
    def get_role_list(names):
        return [roles[name] for name in names if name in roles]

    exec_g = get_role_list(["Director of Intelligence", "Deputy Director", "Executive Oversight Authority"])
    senior_g = exec_g + get_role_list(["Chief of Intelligence", "Chief of Internal Affairs"])
    all_cmd = senior_g + get_role_list(["Intelligence Commander", "Internal Affairs Commander"])
    intel_div = get_role_list(["Intelligence Commander", "Senior Intelligence Analyst", "Intelligence Analyst"])
    ia_div = get_role_list(["Internal Affairs Commander", "Senior IA Investigator", "IA Investigator"])

    async def create_chan(name, category, overwrites, is_voice=False):
        if is_voice:
            await guild.create_voice_channel(name, category=category, overwrites=overwrites)
        else:
            ch = await guild.create_text_channel(name, category=category, overwrites=overwrites)
            await ch.send("placeholder")
        await asyncio.sleep(0.3)

    try:
        # 1. CORE
        cat_core = await guild.create_category("📌 CORE")
        await asyncio.sleep(0.3)
        ow_w = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        if "Verified Personnel" in roles: ow_w[roles["Verified Personnel"]] = discord.PermissionOverwrite(view_channel=True, send_messages=False)
        await create_chan("gis│welcome", cat_core, ow_w)
        
        ow_d = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        for r in senior_g: ow_d[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_chan("gis│directives", cat_core, ow_d)

        ow_a = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False)}
        for r in exec_g: ow_a[r] = discord.PermissionOverwrite(send_messages=True, view_channel=True)
        await create_chan("gis│announcements", cat_core, ow_a)

        # 2. COMMAND HQ
        cat_cmd = await guild.create_category("🚨 COMMAND")
        await asyncio.sleep(0.3)
        ow_hc = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in exec_g: ow_hc[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_chan("gis│high-command", cat_cmd, ow_hc)

        # 3. OPERATIONS
        cat_ops = await guild.create_category("⚡ OPERATIONS & INTEL")
        await asyncio.sleep(0.3)
        ow_ops = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in all_cmd + intel_div: ow_ops[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_chan("gis│operations", cat_ops, ow_ops)
        
        ow_ir = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in intel_div: ow_ir[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_chan("gis│intel-reports", cat_ops, ow_ir)

        # 4. INTERNAL CONTROL
        cat_ic = await guild.create_category("🛡️ INTERNAL CONTROL")
        await asyncio.sleep(0.3)
        ow_ia = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        for r in ia_div: ow_ia[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_chan("gis│internal-affairs", cat_ic, ow_ia)

        # 5. GENERAL COMM LINE
        cat_comm = await guild.create_category("💬 COMMUNICATION")
        await asyncio.sleep(0.3)
        ow_gen = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        if "Verified Personnel" in roles: ow_gen[roles["Verified Personnel"]] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await create_chan("gis│general", cat_comm, ow_gen)
        await create_chan("gis│briefing-room", cat_comm, ow_gen, is_voice=True)

        await ctx.send("✅ **Channels & Permissions structural matrix deployed!** Final step: `!setup_webhooks`")

    except Exception as e:
        await ctx.send(f"❌ Error during channel setup: {e}")


# ==========================================
# COMMAND 3: !setup_webhooks
# ==========================================
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_webhooks(ctx):
    guild = ctx.guild
    await ctx.send("🔌 **Step 3/3:** Injecting safe webhooks into active data log channels...")

    target_channels = ["gis│announcements", "gis│high-command", "gis│intel-reports", "gis│internal-affairs"]
    success_count = 0

    for channel in guild.text_channels:
        if channel.name in target_channels:
            try:
                await channel.create_webhook(name=f"{channel.name.replace('│', '-')}-Hook")
                success_count += 1
                await asyncio.sleep(0.5)
            except Exception:
                continue

    await ctx.send(f"🏆 **System deployment fully finalized!** Successfully built webhooks across {success_count} internal lines.")
    
    # Nuke original staging grounds safely
    try:
        await ctx.channel.delete()
    except Exception:
        pass

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
