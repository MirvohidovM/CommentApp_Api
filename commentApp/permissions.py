from rest_framework.permissions import BasePermission

class IsAuthorUser(BasePermission):
   def has_permission(self, request, view):
       if request.user == request.author:
           return True
       return False