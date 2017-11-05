"""
    ให้ Map Emoji เข้ากับอารมณ์ความรู้สึกลงใน Dict มีรายการดังนี้:
    1. happy (smile)
    2. funny (laught)
    3. sad (cry)
    4. bad ( :( )
    5. love
    6. disapointed (bored)
    7. angry (+evil)
    8. amazed
    9. sleepy
    10. sick (ill)
    11. hungry
    12. lookingup (มองบน 🙄🙄🙄 ตัวนี้ตัวเดียว)
    13. aunji (💩💩💩 ตัวนี้ตัวเดียว)
    14. thankyou
    15. like
    16. dislike
    18. OK
    17. middlefinger
    18. chill
    หรือถ้ามีอีโมจิตัวไหนไม่เข้าในหมวดใดเลย ใส่มาได้เลยครับ
"""

def emotion():
    emotion_mapping = {"😀":"happy",
    "😃":"happy",
    "😄":"happy",
    "😁":"happy",
    "😆":"funny",
    "😅":"funny",
    "😂":"funny",
    "🤣":"funny",
    "😊":"happy",
    "😇":"happy",
    "🙂":"happy",
    "🙃":"funny",
    "😉":"happy",
    "😌":"disapointed",
    "😍":"love",
    "😘":"love",
    "😗":"chill",
    "😙":"chill",
    "😚":"chill",
    "😋":"happy",
    "😜":"funny",
    "😝":"funny",
    "😛":"funny",
    "🤑":"hungry",
    "🤗":"happy",
    "🤓":"chill",
    "😎":"chill",
    "🤡":"happy",
    "🤠":"happy",
    "😏":"disapointed",
    "😒":"disapointed",
    "😞":"disapointed",
    "😔":"disapointed",
    "😟":"amazed",
    "😕":"amazed",
    "🙁":"bad",
    "😣":"angry",
    "😖":"bad",
    "😫":"disapointed",
    "😩":"disapointed",
    "😤":"angry",
    "😠":"angry",
    "😡":"angry",
    "😶":"disapointed",
    "😐":"disapointed",
    "😑":"disapointed",
    "😯":"amazed",
    "😦":"amazed",
    "😧":"amazed",
    "😮":"amazed",
    "😲":"amazed",
    "😵":"sick",
    "😳":"happy",
    "😱":"sick",
    "😨":"amazed",
    "😰":"sick",
    "😢":"sad",
    "😥":"sad",
    "🤤":"hungry",
    "😭":"sad",
    "😓":"bad",
    "😪":"sleepy",
    "😴":"sleepy",
    "🙄":"lookingup",
    "🤔":"amazed",
    "🤥":"amazed",
    "😬":"angry",
    "🤐":"bad",
    "🤢":"sick",
    "🤧":"sick",
    "😷":"sick",
    "🤒":"sick",
    "🤕":"sick",
    "😈":"angry",
    "👿":"angry",
    "👹":"angry",
    "👺":"angry",
    "💩":"aunji",
    "😺":"funny",
    "😸":"funny",
    "😹":"funny",
    "😻":"love",
    "😼":"angry",
    "😽":"chill",
    "🙀":"amazed",
    "😿":"sad",
    "😾":"angry",
    "👐":"chill",
    "🙌":"chill",
    "👏":"like",
    "🙏":"thankyou",
    "👍":"like",
    "👎":"dislike",
    "🤘":"like",
    "👌":"OK",
    "🖕":"middlefinger",
    "💛":"love",
    "💚":"love",
    "💙":"love",
    "💜":"love",
    "🖤":"love",
    "💕":"love",
    "💞":"love",
    "💓":"love",
    "💗":"love",
    "💖":"love",
    "💘":"love",
    "💝":"love",
    "💟":"love"
}
