from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from aiogram.types import FSInputFile
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")         

bot = Bot(token=TOKEN)
dp = Dispatcher()
async def set_bot_description():
    full_description = (
        "💬 99POW Official Support, 24/7 ready to assist with 🎁 bonus claiming, "
        "💰 deposits & withdrawals, 🎮 promos & game inquiries.⚠️\n\n"
        "We will never ask for your account, password, or OTP.📲\n\n"
        "Contact us via website live chat or official Telegram / Facebook — "
        "always online, instant response!\n\n"
        "👑 99POW — All in One. All in 99POW"
    )
    short_description = "99POW Official Support • 24/7 • Instant Help"

    await bot.set_my_description(full_description)
    await bot.set_my_short_description(short_description)

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Telegram Community Special Bonus 🎁", callback_data="special_bonus")],
        [InlineKeyboardButton(text="💰 Deposit / Top-up", callback_data="deposit")],
        [InlineKeyboardButton(text="💸 Withdrawal / Cash out", callback_data="withdraw")],
        [InlineKeyboardButton(text="📱 App Download FREE", callback_data="app_download")],
        [InlineKeyboardButton(text="😲 Balance Missing", callback_data="balance_missing")],
        [InlineKeyboardButton(text="🎁 Bonuses / Promotions", callback_data="bonus")],
        [InlineKeyboardButton(text="🔑 Login / Account Issue", callback_data="login")],
        [InlineKeyboardButton(text="🤝 Business Partnership / Agent", callback_data="agent")],
        [InlineKeyboardButton(text="❓ Others", callback_data="others")],
    ])
# ——————————————— OTHERS – sends text + local image ———————————————
@dp.callback_query(F.data == "others")
async def others(call: types.CallbackQuery):
    text = (
        "Hello fam 👋 For other concerns, please ask <a href='https://chat.wellytalk.com/MDE5YTM4NGQtNGNkYi03MWVlLWJjOGEtZWI4ZjQ4OTRiNTExfDM0ZjY3OTEzYjM4NWYwMGM0NDNjNzVlZjA1NGYzODNhYmQ3ZmY4NDE2ZDQ0NmFjOTgxMzAxM2Y1MGM5YWVlNmM='>Customer service</a> for help\n\n"
        "👉 To speed up our response, kindly provide your member ID.\n"
        "Rest assured, our team will handle your request as a priority and assist you right away.💖"
    )

    photo_path = os.path.join(os.path.dirname(__file__), "images", "support.jpg")
    await call.answer()  # stop loading

    # Just send a new message — never edit or delete anything
    if os.path.exists(photo_path):
        await call.message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=text,
            parse_mode="HTML",
        )
    else:
        await call.message.answer(text)

# ——————————————— BUSINESS PARTNERSHIP / AGENT INQUIRY ———————————————
@dp.callback_query(F.data == "agent")
async def agent_inquiry(call: types.CallbackQuery):
    text = (
        "🤝 Business Partnership / Agent Inquiry\n\n"
        "Hello fam  👋 Thank you for your interest in partnering with 99POW! 💖\n\n"
        "We are only open to players with some online promotion experience.\n"
        "If you encounter any non-agent issues, please contact CSR for a faster and better solution.\n\n"
        "To help us understand better, could you please share:\n"
        " 1️⃣ Your promotion experience (e.g., social media, community groups, offline marketing)\n"
        " 2️⃣ What kind of collaboration or support you are looking for from us\n\n"
        "Once we receive your details, our team will review and guide you on how to start earning as our official 🚀"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Official Agent Channel", url="https://t.me/PHP99POWAGENT")],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ——————————————— LOGIN / ACCOUNT ISSUE MAIN MENU ———————————————
@dp.callback_query(F.data == "login")
async def login_main(call: types.CallbackQuery):
    text = (
        "🔑Login / Account Issue\n\n"
        "🔒Forgot Password\n"
        "👉 Player cannot remember their password and needs reset help.\n\n"
        "☎️ Wrong / Lost Phone Number\n"
        "👉 Player changed/lost their phone number and cannot log in.\n\n"
        "📱 SMS / OTP Not Received\n"
        "👉 Player did not get the code needed for login.\n\n"
        "🚫 Account Locked\n"
        "👉 Player's account is blocked due to multiple failed attempts or security reasons.\n\n"
        "📊 Why Did My Turnover Increase?\n"
        "👉 Player wants to know why their wagering/turnover requirement went up.\n\n"
        "❓ Other Login Problems\n"
        "👉 For any login issue not listed above."
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔒 Forgot Password", callback_data="login_forgot_pw")],
        [InlineKeyboardButton(text="☎️ Wrong / Lost Phone Number", callback_data="login_lost_phone")],
        [InlineKeyboardButton(text="📱 SMS / OTP Not Received", callback_data="login_no_otp")],
        [InlineKeyboardButton(text="🚫 Account Locked - Solution", callback_data="login_locked")],
        [InlineKeyboardButton(text="◀️ Back to Main Menu", callback_data="main_menu")]
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ——————————————— DETAILED RESPONSES (your exact text) ———————————————
@dp.callback_query(F.data == "login_forgot_pw")
async def login_forgot_pw(call: types.CallbackQuery):
    text = ("Forgot Password\n\n"
            "Hello fam You can reset your password by clicking “Forgot Password” on the login page.\n\n"
            "Follow the steps and you'll be back in within seconds!")
    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="login")]]))
    await call.answer()

@dp.callback_query(F.data == "login_no_otp")
async def login_no_otp(call: types.CallbackQuery):
    text = ("SMS / OTP Not Received\n\n"
            "Hello fam  👋 Sometimes SMS/OTP delay is due to network or carrier issue.\n\n"
            "Please wait a few minutes, then request again.\n"
            "Still not received? Reach out to Customer Service for assistance")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Contact Customer Service Now",
            url="https://chat.wellytalk.com/MDE5YTM4NGQtNGNkYi03MWVlLWJjOGEtZWI4ZjQ4OTRiNTExfDM0ZjY3OTEzYjM4NWYwMGM0NDNjNzVlZjA1NGYzODNhYmQ3ZmY4NDE2ZDQ0NmFjOTgxMzAxM2Y1MGM5YWVlNmM="          # ← change this link anytime
        )],
        [InlineKeyboardButton(text="Back", callback_data="login")]
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "login_locked")
async def login_locked(call: types.CallbackQuery):
    text = ("🚫 Account Locked - Solution\n\n"
            "Hi fam👋 Your account may be locked for several reasons:\n"
            "• Multiple wrong login attempts\n"
            "• Security protection\n"
            "• Violation of platform rules\n\n"
            "Don't worry — your funds are 100% safe!\n"
            "👉 Just send us your username/member ID and we'll unlock it for you in minutes.")
    await call.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="login")]]))
    await call.answer()
# ─────────────────────── BONUSES / PROMOTIONS MAIN ──────────────────────
@dp.callback_query(F.data == "bonus")
async def bonus_main(call: types.CallbackQuery):
    text = (
        "🎁 Treasure Box Event\n"
        "Finish daily tasks = ₱100 bonus daily.\n\n"
        "🤝 Agent Program\n"
        "Invite friends = ₱77-₱188 each + rebates + big rewards.\n\n"
        "💎 Combined Earnings\n"
        "Daily tasks + invites = ₱5,310-₱8,640/month (or more).\n\n"
        "🚀 How to Earn\n"
        "Do tasks, invite friends, stay active = earn nonstop."
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Treasure Box Event", callback_data="treasure_box")],
        [InlineKeyboardButton(text="🤝 Agent Program", callback_data="agent_program")],
        [InlineKeyboardButton(text="💎 Combined Earnings", callback_data="combined_earnings")],
        [InlineKeyboardButton(text="🚀 Refer and Earn Instantly", callback_data="refer_earn")],
        [InlineKeyboardButton(text="◀️ Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ─────────────────────── 1. TREASURE BOX EVENT (100% done) ──────────────────────
@dp.callback_query(F.data == "treasure_box")
async def treasure_box(call: types.CallbackQuery):
    text = (
        "🎁 Treasure Box Event\n\n"
        "Hello fam 👋 Don't miss our 99POW Treasure Box Event!\n\n"
        "Complete the daily treasure box tasks and get a ₱100 guaranteed bonus every single day\n\n"
        "👉 That's ₱3,000 in just 1 month if you stay consistent!\n\n"
        "No luck needed — just finish your tasks and enjoy real rewards.\n\n"
        "🔥 Act now: Open your treasure box today, don't let your ₱100 slip away!"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back to Bonuses", callback_data="bonus")],
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ─────────────────────── 2. AGENT PROGRAM ──────────────────────
@dp.callback_query(F.data == "agent_program")
async def agent_program(call: types.CallbackQuery):
    text = (
        "🤝 Agent Program\n\n"
        "Hi fam 👋 Want to earn not just from playing, but also by sharing? Join the 99POW Agent Program today!\n\n"
        "✨ Rewards you can get:\n"
        "One-time Invite Bonus: ₱77 - ₱188 per friend\n"
        "Achievement Rewards: ₱100 up to ₱25,000,000\n"
        "Daily Commission: up to 1% rebate from your downline's deposits/bets\n\n"
        "👉 Example: Invite 30 friends = ₱2,310 - ₱5,640 instant bonus.\n\n"
        "🚀 Start inviting now — the more friends you bring, the more cash flows into your pocket!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="bonus")]])
    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ─────────────────────── 3. REFER & EARN INSTANTLY ──────────────────────
@dp.callback_query(F.data == "refer_earn")
async def refer_earn(call: types.CallbackQuery):
    text = (
        "🎉 REFER & EARN INSTANTLY! 🎉\n\n"
        "Walang kailangan na application — anyone can be an Agent!\n\n"
        "Mag-imbita ng mga kaibigan at kumita ng up to ₱180 kada player — may instant bonus pa! 💸\n\n"
        "💥 One-time bonus para sa bawat naimbitang player\n"
        "💬 Invite must deposit at least ₱200\n"
        "🔁 Turnover requirement: 5x lang!\n"
        "🎮 Valid games: Electronic Slots at Fishing\n"
        "⚡️ Crediting: Daily at automatic na pumapasok within 24 hours\n"
        "📈 Mas maraming invites = mas malaking kita!\n\n"
        "📲 I-share na ang iyong referral link at magsimulang kumita! 💰\n\n"
        "📢 Para sa updates at promos, sumali sa official Telegram channel:\n"
        "t.me/VIP99POWCHANNEL\n\n"
        "✨ All in One. All in 99POW."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="bonus")]])
    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── 4. COMBINED EARNINGS ──────────────────────
@dp.callback_query(F.data == "combined_earnings")
async def combined_earnings(call: types.CallbackQuery):
    text = (
        "💎 Combined Earnings — 1 Month Projection\n\n"
        "By joining both activities, you double your rewards with the same effort.\n\n"
        "Example (30 days active + 30 invited friends):\n"
        "Treasure Box Daily Bonus = ₱100 x 30 = ₱3,000\n"
        "Agent Invite Bonus = ₱77 - ₱188 x 30 = ₱2,310 - ₱5,640\n\n"
        "➡️ Total Monthly Earnings = ₱5,310 - ₱8,640 💖\n\n"
        "💡 And that's just the beginning! This projection does not yet include:\n"
        "Rebates up to 1% from your team's deposits/bets\n"
        "Achievement Rewards up to ₱25,000,000\n\n"
        "👉 That means your real earnings can go way beyond ₱8,640! 🚀\n\n"
        "🔥 Don't wait: Start your daily treasure box + invite friends today, and watch your income grow every day."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="bonus")]])
    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()
    
# ─────────────────────── BALANCE MISSING ──────────────────────
@dp.callback_query(F.data == "balance_missing")
async def balance_missing(call: types.CallbackQuery):
    text = (
        "💳 Balance Suddenly Missing\n\n"
        "Hello fam 👋 No need to worry 💖 Sometimes this happens because of the game provider's technical issue.\n\n"
        "Usually, your balance will return to your wallet within 5 minutes to 3 hours after the maintenance ends.\n\n"
        "👉 If your funds have not returned after this time, please provide your member name/ID and our CSR team will assist you right away to resolve it. 🚀"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="RECALL BALANCE GUIDE", callback_data="recall_guide")],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── RECALL BALANCE GUIDE (your exact Filipino message) ──────────────────────
@dp.callback_query(F.data == "recall_guide")
async def recall_guide(call: types.CallbackQuery):
    guide = (
        "Hi 99POW Fam!\n"
        "Nawawala ba ang inyong balance pagkatapos maglaro ng isang game? 😟 Don't worry — safe na safe po ang funds ninyo!\n\n"
        "Para maibalik ang inyong balance, sundin lang ang mga simpleng steps:\n"
        "1️⃣ Pumunta sa Withdrawal section\n"
        "2️⃣ I-tap ang Recall Balance\n"
        "3️⃣ At agad pong babalik ang inyong funds sa inyong wallet!\n\n"
        "Walang dapat ipag-alala — lahat ng funds ninyo ay secured sa amin.\n\n"
        "Kung may mga katanungan pa kayo o kailangan ninyo ng tulong, huwag mahiyang mag-contact sa aming Customer Service. Lagi kaming handang tumulong!\n\n"
        "🙏 Salamat sa patuloy na pagtangkilik!\n"
        "✨ All in One. All in 99POW. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="balance_missing")],
    ])

    await call.message.edit_text(guide, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── APP DOWNLOAD FREE ──────────────────────
@dp.callback_query(F.data == "app_download")
async def app_download(call: types.CallbackQuery):
    text = (
        "Hello fam 👋 Thank you for downloading the 99POW App!\n\n"
        "You'll receive ₱5 bonus + 3 free spins right away. 🎁\n\n"
        "⚠️ Reminder: If you don't make a deposit, withdrawals are not possible.\n\n"
        "👉 We strongly recommend making at least one deposit first to activate withdrawals, "
        "then enjoy your free bonus and spins.\n\n"
        "Start now, deposit once, and maximize your rewards with the 99POW Family! 🚀💖"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Download App Now", url="https://99pow.com/app")],  # Change link if needed
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── WITHDRAWAL SECTION ──────────────────────
@dp.callback_query(F.data == "withdraw")
async def withdraw_main(call: types.CallbackQuery):
    text = (
        "For deposit or withdrawal concerns, please send us your username and briefly describe the issue so we can assist you faster.\n\n"
        "👉 Our support team will guide you step by step.\n\n"
        "Hello fam 👋 Normally, withdrawal review takes within 10 minutes.\n"
        "Once approved, the bank transfer also arrives within 10 minutes.\n\n"
        "⏳ If it takes longer, possible reasons are:\n"
        "Our Risk Control Team is doing a second review, which may take 2-10 hours.\n"
        "If already approved but not credited within 10 minutes, it is due to the bank's processing time.\n\n"
        "Please don't worry — your funds are 100% safe and will arrive soon. 💖 Kindly wait patiently."
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="HOW TO WITHDRAW?", callback_data="how_to_withdraw")],
        [InlineKeyboardButton(text="BINDING WITHDRAWAL ACCOUNT ISSUES", callback_data="binding_issues")],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

@dp.callback_query(F.data == "how_to_withdraw")
async def how_to_withdraw(call: types.CallbackQuery):
    text = (
        "💸 Paano Mag-Withdraw sa 99POW\n\n"
        "Step 1. Buksan ang 99POW app → Withdrawal.\n"
        "Step 2. Piliin ang payout method (GCash/Maya).\n\n"
        "📌 Kung first time mag-withdraw:\n"
        "• Full Name (pareho sa E-wallet, 4-50 characters, hindi na mababago after submitting).\n"
        "• Account Number (GCash/Maya no., tamang format: ✅ 09XXXXXXXXX, sa madaling salita 11 NUMBERS).\n\n"
        "Step 3. Gumawa ng Transaction Password (6 characters ONLY using letters/numbers, at dapat iba sa login password).\n"
        "Step 4. Ilagay ang amount (min: 100 | max: 50,000).\n"
        "Step 5. Double-check details → Withdraw/Confirm.\n"
        "Step 6. Kung may OTP/PIN, ilagay.\n"
        "Step 7. Hintayin ang status: Processing → Success.\n"
        "Step 8. I-check ang balance sa GCash/Maya.\n\n"
        "⚠️ Paalala:\n"
        "• ✅ Dapat eksaktong tugma ang Full name sa E-wallet na ilalagay mo.\n"
        "• ✅ Dapat tama at eksaktong Account Number (GCash/Maya number) ang ilalagay, dahil doon mismo papasok ang I-wiwithdraw mo.\n"
        "• ✅ Dapat 6 characters ONLY using letters at numbers sa Transaction Password.\n"
        "• 🔒 Magkaiba ang Account at Transaction password.\n"
        "• 🔒 Isang E-wallet lang bawat 99POW account para maiwasan ang withdrawal errors na hindi sinasadya.\n"
        "• ❌ Huwag ilagay ang phone number bilang Full name, dahil magkaka-issue kayo sa withdrawal.\n"
        "• ✔️ Ang OTP ay valid lang for a few minutes — i-enter agad bago mag-expire.\n\n"
        "📢 Sumali sa Telegram para sa promos/updates:\n"
        "👉 t.me/VIP99POWCHANNEL\n\n"
        "✨ All in One. All in 99POW. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

@dp.callback_query(F.data == "binding_issues")
async def binding_issues(call: types.CallbackQuery):
    text = (
        "💳 Paano Mag-Bind ng E-Wallet sa 99POW\n\n"
        "⚠️ Hello 99POW Fam!\n\n"
        "1. Open ang 99POW App → punta sa \"Withdrawal\".\n"
        "2. Pindutin ang \"+\".\n"
        "3. Fill out ang mga required details:\n"
        "Full name of the payee • katulad sa E-WALLET mo (See image below for example/guide)\n"
        "• ⚠️ Once submitted, hindi na mababago o ma-eedit ito sa current E-wallet mo.\n"
        "• ✅ Dapat eksaktong tugma ang Full name sa E-wallet na ilalagay mo.\n"
        "• ✅ Wag lalagpas sa 30 na letters, at walang special characters tulad ng tuldok/period.\n"
        "• ❌ Huwag ilagay ang phone number bilang Full name, dahil magkaka-issue kayo sa withdrawal.\n"
        "• E-Wallet Type, Choose GCASH or MAYA.\n"
        "• Account Number, GCASH/MAYA mobile number\n\n"
        "👉 Example: \n"
        "TAMA: ✅ 09123456789\n"
        "MALI:  ❌ 9123456789\n\n"
        "• Transaction Password\n"
        "👉 Please enter 6 characters using ONLY letters and numbers. No special characters allowed.\n"
        "⚠️ Login password and Transaction password cannot be the same, make sure they are different.\n"
        "✅ Kailangan magkaiba para mas secure ang account — kung makuha man ang login mo, hindi agad magagalaw ang withdrawals mo.\n\n"
        "4. Tap Submit para ma-bind successfully.\n\n"
        "✅ Lalabas ang confirmation message kapag successful na ang binding.\n\n"
        "⚠️ STRICTLY ONE E-WALLET PER 99POW ACCOUNT TO AVOID ERRORS AND FAILURES. ⚠️\n\n"
        "📌 Tip: Always double-check ang Full name at Account Number bago mag-submit to avoid future errors.\n\n"
        "✨ All in One. All in 99POW. ✨"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="withdraw")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── DEPOSIT SECTION (already working) ──────────────────────
@dp.callback_query(F.data == "deposit")
async def deposit_main(call: types.CallbackQuery):
    text = (
        "Deposit / Top-up\n\n"
        "Hello fam 👋  Deposits normally arrive within 10 minutes.\n\n"
        "If there's any delay, it's usually because of the bank side issue, "
        "but don't worry — your funds are 100% safe and will not be lost. 💖\n\n"
        "👉 If your deposit hasn't arrived after 10 minutes, please send us your payment proof/receipt "
        "so we can assist you right away. 🚀"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="HOW TO DEPOSIT?", callback_data="how_to_deposit")],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])

    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

@dp.callback_query(F.data == "how_to_deposit")
async def how_to_deposit(call: types.CallbackQuery):
    text = (
        "Paano Mag-Deposit sa 99POW\n\n"
        "1. Buksan ang 99POW app.\n"
        "2. Sa home page, tap \"Deposit.\"\n"
        "3. Piliin ang payment method mo (GCash o Maya).\n"
        "4. Pili ng available payment channel.\n"
        "5. I-type ang amount na gusto mong i-deposit.\n"
        "6. (Optional) Pili ng promo kung meron. Tap \"Next.\"\n"
        "7. Hintayin ang QR code o payment instructions.\n"
        "8. Bayaran gamit ang GCash, Maya, o bank app (scan o copy details).\n"
        "9. Hintayin ang \"Payment Successful\" na prompt.\n"
        "10. Tap \"Done\" - automatic na mag-u-update ang balance mo.\n\n"
        "📢 Huwag kalimutang sumali sa official Telegram channel para sa promos at updates:\n"
        "👉 t.me/VIP99POWCHANNEL\n\n"
        "✨ All in One. All in 99POW!"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="deposit")],
    ])

    await call.message.edit_text(text, reply_markup=kb, disable_web_page_preview=True)
    await call.answer()

# ─────────────────────── SPECIAL BONUS SECTION (already working) ──────────────────────
@dp.callback_query(F.data == "special_bonus")
async def special_bonus(call: types.CallbackQuery):
    text = (
        "Hello fam 👋 Good news from the 99POW Family! 💖\n\n"
        "Just download the 99POW App and make a deposit of ₱200, and you'll receive an extra bonus code:\n\n"
        "QV0FOTDV\n\n"
        "👉 Don't miss this chance  🚀— download now, deposit today, and claim your exclusive reward!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Download app for free", url="https://99pow.com/app")],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data="main_menu")],
    ])
    await call.message.edit_text(text, reply_markup=kb)
    await call.answer()

# ─────────────────────── BACK TO MAIN MENU ──────────────────────
@dp.callback_query(F.data == "main_menu")
async def back_to_main(call: types.CallbackQuery):
    await call.message.edit_text(
        "🌟 99POW Quick Reply Menu - Explanations\n\n"
        "💰 Deposit / Top-up - For checking your deposits, delays, or payment concerns.\n\n"
        "💸 Withdrawal / Cash out - For withdrawal status, delays, or bank transfer issues.\n\n"
        "🎁 Bonuses / Promotions - For claiming or asking about rewards, promos, and events.\n\n"
        "🔑 Login / Account Issue - For help with login, password, or account access.\n\n"
        "📱 App Download / Technical Support - For installing the 99POW app or fixing technical problems.\n\n"
        "🤝 Business Partnership / Agent Inquiry - For partnership opportunities and agent program details.\n\n"
        "❓ Others - For any concerns not listed above.\n\n",
        reply_markup=main_menu()
    )
    await call.answer()

# ─────────────────────── CATCH ALL OTHER BUTTONS (temporary) ──────────────────────
@dp.callback_query()
async def catch_all(call: types.CallbackQuery):
    await call.answer("This section is coming very soon!", show_alert=True)

# ─────────────────────── START COMMAND ──────────────────────
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🌟 99POW Quick Reply Menu - Explanations\n\n"
        "💰 Deposit / Top-up - For checking your deposits, delays, or payment concerns.\n\n"
        "💸 Withdrawal / Cash out - For withdrawal status, delays, or bank transfer issues.\n\n"
        "🎁 Bonuses / Promotions - For claiming or asking about rewards, promos, and events.\n\n"
        "🔑 Login / Account Issue - For help with login, password, or account access.\n\n"
        "📱 App Download / Technical Support - For installing the 99POW app or fixing technical problems.\n\n"
        "🤝 Business Partnership / Agent Inquiry - For partnership opportunities and agent program details.\n\n"
        "❓ Others - For any concerns not listed above.\n\n",
        reply_markup=main_menu()
    )
async def on_startup():
    await set_bot_description()

async def main():
    dp.startup.register(on_startup)
    print("99POW Bot running!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
