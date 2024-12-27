# BOTUN KAYNAK KODLARI ZEUS289 TARAFINDAN PUBLANMIŞTIR.

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) # SEX NOKTASI AMINA KOYİM BURADA NEYLE CALISCAKSA YAP 

letters = []
channel_id = KANAL İDİ BUDA YOKSA none YAZ 
admin_ids = [ADMİN İD YANİ KENDİ İDN ]

@bot.event
async def on_ready():
    print(f'🎅 {bot.user} olarak giriş yapıldı!')
    print(f'🎄 Bot sunucuya başarıyla bağlandı!')
    activity = discord.Game(name="Noel Baba'ya Mektup Yazıyor 🎁")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send("🎅 **Bot çalışıyor!** 🎄")

@bot.command()
async def mektup(ctx, *, letter: str):
    user = ctx.author
    letters.append({'user': user.name, 'letter': letter})
    await ctx.send(
        f"🎄 **Teşekkürler {user.name}!** Mektubun Noel Baba'ya gönderildi! 🎁\n"
        f"✨ Yazdığın mektubu admin kontrol edebilir."
    )

@bot.command()
async def aç(ctx):
    if ctx.author.id not in admin_ids:
        await ctx.send("🚫 **Bu komutu yalnızca yetkili adminler kullanabilir!**")
        return

    if not letters:
        await ctx.send("🎅 **Hiç mektup bulunamadı!** 🎄")
        return

    await ctx.send("🎁 **Noel Baba'ya Yazılan Mektuplar:**")
    for letter in letters:
        await ctx.send(f"🎄 **{letter['user']}**:\n📜 {letter['letter']}")

@bot.command()
@commands.has_permissions(administrator=True)
async def sunucu_kanal_id(ctx, kanal_id: int):
    global channel_id
    channel_id = kanal_id
    await ctx.send(f"🎄 **Mektuplar artık `{kanal_id}` kanalına gönderilecek!** 🎁")

@bot.command()
async def gönder(ctx):
    if ctx.author.id not in admin_ids:
        await ctx.send("🚫 **Bu komutu yalnızca yetkili adminler kullanabilir!**")
        return

    if not letters:
        await ctx.send("🎅 **Henüz yazılmış bir mektup yok!** 🎄")
        return

    channel = bot.get_channel(channel_id)
    if channel is None:
        await ctx.send("🚫 **Geçersiz kanal ID'si!** Lütfen doğru bir kanal ID girin.")
        return

    for letter in letters:
        await channel.send(
            f"🎄 **{letter['user']} tarafından yazılan mektup:**\n📜 {letter['letter']}"
        )

    letters.clear()
    await ctx.send("🎅 **Tüm mektuplar başarıyla gönderildi!** 🎁")

@bot.command()
async def zar(ctx):
    dice = random.randint(1, 6)
    await ctx.send(f"🎲 Zar atıldı! Sonuç: **{dice}**")

@bot.command()
async def espri(ctx):
    jokes = [
        "Benim matematikle aramda bir problem var. Hep beni bölüyor. 🤓",
        "Kediler neden kahve içemez? Çünkü köpüğü bozarlar! ☕",
        "Kopya çekmek yasak dediler. O yüzden arkadaşımın kağıdına 'Alıntıdır' yazdım. 😂",
        "Çay bardağı neden ağladı? Çünkü demlik onu terk etti. 😢",
        "Sınavda çok heyecanlandım, kalem kağıda düello teklif etti. 🤺",
        "Gitar neden üzgündü? Çünkü bir teli koptu ve akordu bozuldu. 🎸",
        "Bilgisayarımı neden denize attım? Çünkü internete bağlanmak istedim! 🌊",
        "Fazla espri yazmıyorum, çünkü bir günde çok güldürmek istemiyorum. 😎",
    ]
    joke = random.choice(jokes)
    await ctx.send(f"😂 **Espri zamanı!** {joke}")

@bot.command()
async def şans(ctx):
    outcomes = ["🍀 Şanslısın! Bugün güzel şeyler olacak. ✨", 
                "😕 Şanssızsın. Ama üzülme, her şey düzelir! 🌈",
                "🤷 Şansın nötr bugün. Ne iyi ne kötü!",
                "🎉 Bugün çok şanslısın! Milli piyango bileti almayı unutma. 😉",
                "💔 Bugün şanssızsın. Ama kötü günler de geçer!"]
    outcome = random.choice(outcomes)
    await ctx.send(outcome)

@bot.command()
async def tokat(ctx, member: discord.Member):
    await ctx.send(f"🤚 **{ctx.author.name}, {member.mention} kişisine kocaman bir tokat attı!** 💥")

@bot.command()
async def hack(ctx, member: discord.Member):
    await ctx.send(f"💻 **{member.name} hackleniyor...** Lütfen bekleyin.")
    steps = [
        f"🔍 IP adresi bulunuyor... {random.randint(100, 999)}.***.***.***",
        "📂 Dosyalar indiriliyor... %25",
        "📂 Dosyalar indiriliyor... %50",
        "📂 Dosyalar indiriliyor... %75",
        "📂 Dosyalar indiriliyor... %100",
        "🛡️ Güvenlik duvarı aşıldı!",
        "🔐 Şifreler çözülüyor...",
        f"✅ Hack tamamlandı! {member.name}'in tüm sırları ortaya çıktı. Ama bu sadece bir şaka! 😄"
    ]
    for step in steps:
        await ctx.send(step)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("🚨 **Hata:** Komutun tüm parametrelerini doldurun!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 **Bu komutu sadece adminler kullanabilir!** 🎅")
    else:
        await ctx.send("❌ **Bir hata oluştu!**")

bot.run('TOKENİNİ BURAYA GİRCEN KNK ')