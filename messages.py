from settings import *
from functions import *
import settings

START = f'🙋‍♂ "Sub Coin" botiga xush kelibsiz! Bu bot sizga kanalga o‘zaro obunachilar yig‘ishda yordam beradi. Boshlashdan oldin iltimos, [foydalanish qo‘llanmasi va qoidalar]({LINK_TO_INTRODUCTION_AND_RULES}) bilan tanishib chiqing.'

UPDATE = 'Yana salom!'

LITTLE_SUBCOIN_1 = f'❗️Kanalingizni targ‘ib qilish uchun kamida {LITTLE_SUBCOIN_TO_GET_SUBS} ta Sub Coin bo‘lishi kerak!'

LITTLE_SUBCOIN_2 = '😳 Sub Coin yetarli emas!'

SEND_YOUR_CHANNEL = '❕Kanalga obunachilar olish uchun:\n__1) Ushbu botni kanalga qo‘shing;\n2) Kanal foydalanuvchi nomini (username) shu yerga yuboring.__'

def SEND_SUB_COUNT_1(m):
    send_sub_count  = f'😀 Juda yaxshi. Endi qancha obunachi kerakligini yozing.\n*Mavjud balans:* {user_balance(m.from_user.id)}'
    return send_sub_count
    
def NEW_REFERAL(argument):
    new_referal = f'🥳 Tabriklaymiz! Yangi referal qo‘shildi!\nJami referallar: {referals(argument)}'
    return new_referal
    
def PROFILE(m):
    profile = f'👤 Ism: {m.from_user.first_name}\n📟 ID: `{m.from_user.id}`\n💰 Balans: {user_balance(m.from_user.id)} Sub Coin\n💪 Qilingan obunalar: {alltime_subs(m.from_user.id)}\n🤝 Olingan obunachilar: {alltime_get_subs(m.from_user.id)}\n🤥 Jarima miqdori: {fine_count(m.from_user.id)} Sub Coin\n👣 Referallar soni: {referals(m.from_user.id)}'
    return profile

GIVE_CHANNEL_LINK = '''❕*Targ‘ibotni boshlash uchun:*

1) _Ushbu botni kanalga qo‘shing (kanal ochiq bo‘lishi shart);_
2) _Kanal foydalanuvchi nomini yozing. Masalan:_ @SubCoinChannel'''

CANCEL_TEXT = '🎳 Bekor qilindi'

BOT_NOT_IN_CHANNEL = '''❗️❗️❗️Botni kanalga admin sifatida qo‘shmadingiz. Avval botni kerakli kanalga qo‘shing, keyin esa username yuboring❗️❗️❗️\n\n*Bot qo‘shilgandan so‘ng kanal username’sini bu yerga yuboring!*'''

THIS_IS_NOT_CHANNEL = '''😡 *Bu kanal emas!*\nObuna yig‘moqchi bo‘lgan kanal foydalanuvchi nomini yuboring!''' 

THIS_IS_NOT_TEXT = '''🤔 *Bu kanal username’si emas!*\n\nObuna yig‘moqchi bo‘lgan kanal username’sini yuboring.'''

def CONFIRM_ADDING_CHANNEL(username, subcount, price):
    confirm_adding_channel = f'''Targ‘ibot uchun kanal qo‘shilishini tasdiqlang:\n\n📻 Kanal: @{username}\n\n📲 Obunachilar soni: {subcount}\n\n💳 Narx: {price} Sub Coin''' 
    return confirm_adding_channel
    
CHANNEL_ON_PROMOTION = "❗️Bu kanal allaqachon targ‘ib qilinmoqda!"

CHANNEL_ON_PROMOTION_2 = '❌ Ushbu kanal targ‘ibotda. Tugaguncha kuting yoki boshqa kanal yuboring:'

CHANNEL_SUCCESSFULLY_ADED = '👍 Kanal muvaffaqiyatli targ‘ibotga qo‘shildi.'

SUBSCRIBE_ON_THIS_CHANNEL = '''Quyidagi kanalga obuna bo‘ling:\n1️⃣ Kanalga o‘ting 👇, obuna bo‘ling ✔️ va yuqoriga qarab 5-10 postni ko‘zdan kechiring 🔝👁.\n2️⃣ Keyin bu yerga qayting va mukofot oling ⚡️.'''

NO_HAVE_CHANNELS_FOR_SUBSCRIBE = f"😔 Hozircha obuna bo‘lish uchun kanallar yo‘q. Tez orada paydo bo‘ladi!\n\nShu paytda bizning chatimizga qo‘shiling: {LINK_TO_CHAT_OF_BOT}"

def CHANNEL_WAS_DEL_FROM_CHANNEL(id, link_to_rules):
    message =f'❗️Muhim xabar!\n\nBot sizning kanal ({id}) dan o‘chirildi.\n😡 [Qoidalar]({link_to_rules})ga zid harakat uchun targ‘ibot to‘xtatildi va foydalanilmagan Sub Coin’ning yarmi sizga qaytarildi.\nObunachilarni tekshirish ham to‘xtatildi.'
    return message
    
def SUBSCRIBE_IS_SUCCESSFULLY(username):
    message = f'👍 @{username} kanaliga muvaffaqiyatli obuna bo‘ldingiz.\nBalansingizga 1 Sub Coin 💠 qo‘shildi.'
    return message
    
def YOU_ARE_LATE_FOR_SUBS(username):
    message = f'☹️ Siz kech qoldingiz, bu kanalning targ‘iboti tugagan.\n@{username} kanalidan chiqishingiz mumkin.'
    return message
    
YOU_DONT_COMPLETE_SUBS = '😡 Siz hali bu kanalga obuna bo‘lmadingiz!'
    
def PARTNER_PROGRAM(username_of_bot, user_id, ref_count):
    message = f'🤩 Do‘stlaringizni botga taklif qiling va har biri uchun 5 Sub Coin oling.\n👥 Taklif qilinganlar soni: {ref_count}\n👣 Referal havolangiz: https://t.me/{settings.botname}?start={user_id}'
    return message
    
SELECT_ADMIN_MENU_BUTTON = '🛠 Menyudan kerakli bo‘limni tanlang:'
    
START_COLLECT_STAT = '⏱ Statistika yig‘ilmoqda...'

def STATISTICS(all, die):
    alive = all - die
    message = f'😅 Jami foydalanuvchilar: {all}\n\n😵 Nofaol: {die}\n\n🤠 Faol: {alive}'
    return message
   
SEND_MESSAGE_FOR_SEND = '🖋 Yuborish uchun _matn/foto/video/gif/fayl_ yuboring.'

def MAILING_END(all, die):
    alive = all - die
    message = f'✅ Xabarlar yuborildi.\n\n🤠 Yetib borgan: {alive}\n\n😢 Yetib bormagan: {die}'
    return message
    
SEND_USER_FOR_UBAN = '❓Foydalanuvchini ban qilish uchun yuboring:\n\n<ID> 0\n\n❓Unban qilish uchun:\n\n<ID> 1'

NOT_INTEGER = 'Kiritilgan qiymatlardan biri raqam emas!'

LITTLE_VALUE = '😡 Siz ikkita qiymatni bo‘sh joy bilan ajratib yuborishingiz kerak edi!'

YOU_WAS_BANNED = '🥳 Tabriklaymiz! Siz bu botdan foydalana olmaysiz, chunki siz ban qilingansiz.'

YOU_WAS_HACK_ME = '🤭 Siz meni buzib oldingiz! Endi nima qilaman?'

SEND_USER_FOR_CHANGE_BALANCE = '''❗️Foydalanuvchi balansini o‘zgartirish uchun yuboring:\n\n<id> <balans qiymati>'''

def SUBSCRIPTION_VIOLATION(username, sub_term, count_of_fine):
    message = f'😡 Siz @{username} kanalidan {sub_term} kun o‘tmasidan chiqib ketdingiz!\n\nJarima sifatida balansingizdan {count_of_fine} Sub Coin 💠 olib tashlandi.'
    return message
    
YOU_DID_THIS = '🙂 Juda aqlliman dedingmi?\nBu topshiriqni allaqachon bajargansan!'

    


