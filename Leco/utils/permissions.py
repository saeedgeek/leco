from rest_framework.permissions import BasePermission


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            user=request.user
            student=user.student
            if student and user.user_type == "student" :
                return True
            else:
                return False
        except:
            return False