
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "MET_TON_TOKEN_ICI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur Casipere 🤖\n\nJe t'aide a suivre Lucky Jet sans te mentir.\nTape /aide pour voir les commandes.")

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Commencer\n/aide - Voir les commandes\n/conseil - Un conseil honnete")

async def conseil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conseil Casipere : Ne cours jamais apres tes pertes. Fixe une limite avant de jouer et arrete-toi.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("conseil", conseil))
    print("Casipere est lance...")
    app.run_polling()

if __name__ == "__main__":
    main()
*Pour copier :*
Reste appuyé longtemps dessus -> *Copier*

Après va sur GitHub, reste appuyé dans la case blanche -> *Coller*

Tu as réussi à copier ?
