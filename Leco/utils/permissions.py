from rest_framework.permissions import BasePermission


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            student = user.student
            if student and user.user_type == "student":
                return True
            else:
                return False
        except:
            return False


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            teacher = user.teacher
            if teacher and user.user_type == "teacher":
                return True
            else:
                return False

        except:
            return False


# class CenterPermission(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             user = request.user
#             center = user.agent.
#             print(".........................................",center,user.user_type == "center")
#             if center and user.user_type == "center":
#                 print("......................................... center")
#                 return True
#             else:
#                 return False
#
#         except:
#             print("......................................... except")
#             return False
#
#
# class AgentPermission(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             user = request.user
#             agent = user.agent
#             if agent and user.user_type == "agent":
#                 return True
#             else:
#                 return False
#
#         except:
#             return False

