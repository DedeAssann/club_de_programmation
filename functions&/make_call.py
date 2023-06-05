"Making a call using python"

import messagebird

client = messagebird.Client("<api>")

try:
    msg = client.voice_message_create(
        "+50946788890", "Hey you, I heard you needed a call! ", {"voice": "male"}
    )

    print(msg.__dict__)

except messagebird.CLient.ErrorException as e:
    for error in e.errors:
        print(error)
