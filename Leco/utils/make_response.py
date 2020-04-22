from rest_framework.response import Response


def response(condition, message, status):
    try:
        dict(message)

        return Response(message, status=status)

    except:
        s = ""
        if condition == 1:
            s = "ok"
        elif condition == 0:
            s = "bad"

        return Response(
            {"status": s,
             "msg": message

             },
            status=status
        )
