from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core import serializers





def new_user(request):
    pass
    # users = UserBase.objects.all()
    # return render(request, 'new_user.html', {'users': users})

import re
def registration_check2(request):
    pass
#     content = request.GET.get('content')
#     if request.GET.get('action') == 'check_username':
#         it_exists = UserBase.objects.filter(user_name__exact=content).exists()
#         response = JsonResponse({'exists': it_exists})
#     if request.GET.get('action') == 'check_email':
#         it_exists = UserBase.objects.filter(email__exact=content).exists()
#         ends_with = re.search(r'@yahoo.com$|gmail.com$|hotmail.com$', content)
#         print(f'correctly ends_with ({ends_with})')
#         if ends_with != None:
#             result2 = content.split('@')
#             stri1 = ''
#             stri2 = ''
#             for i in result2:
#                 stri1 += i
#             stri1 = stri1.split('.')
#             for i in stri1:
#                 stri2 += i
#             print(f'stripped result ({stri2})')
#             contains_non_alpha_num = re.search(r"\W[-_/]", stri2)
#             print('===============alpha & number container----------------------------')
#             print(contains_non_alpha_num)
#             if contains_non_alpha_num != None:
#                 print('===============yes contains non alpha & digit---------------------')

#                 unwanted_characterz = ['~', '@', '#', '$', '%', '^', '&', '*', '(', ')', \
#                                        '_', '-', '+', '=', '[', ']', '{', '}', '|', '', ":", \
#                                        ";", '"', "'", '<', ",", '>', ".", "/", "?"]
#                 contain_unwanted_characterz = False

#                 contains_the_required_chars = re.search(r"[-_/]", stri2)
#                 print(f'chars_container is ({contains_the_required_chars})')
#                 for i in stri2:
#                     if i in unwanted_characterz:
#                         print('===============it contains the required char---------------------')
#                         contain_unwanted_characterz = True
#                         return JsonResponse({'exists': it_exists})
#                     break
#                 if contains_the_required_chars != None and not contain_unwanted_characterz:
#                     print('===============it contains the required char---------------------')
#                     return JsonResponse({'exists': it_exists})
#         else:
#             return JsonResponse({'exists': it_exists})
#         # re.search(r"content{1}", "geeks")
#         # {p} Matches the expression to its left p times, and not less.
#         # \w Matches alphanumeric characters, that is a - z, A - Z, 0 - 9, and underscore(_)
#         # \W Matches non - alphanumeric characters, that is except a - z, A - Z, 0 - 9 and _
#         # \d Matches digits, from 0-9.
#         # \D Matches any non-digits.
#         # \s Matches whitespace characters, which also include the \t, \n, \r, and space characters.
#         # \S Matches non-whitespace characters.
#         # [a-z0-9]Matches characters from a to z or from 0 to 9.
#         # [(+*)]Special characters become literal inside a set, so this matches (, +, *, or )
#     if request.GET.get('action') == 'check_password':
#         it_exists = UserBase.objects.filter(password__exact=content).exists()
#         if ends_with != None:
#             result2 = content.split('@')
#             stri1 = ''
#             stri2 = ''
#             for i in result2:
#                 stri1 += i
#             stri1 = stri1.split('.')
#             for i in stri1:
#                 stri2 += i
#             print(f'stripped result ({stri2})')
#             contains_non_alpha_num = re.search(r"\W[-_/]", stri2)
#             print('===============alpha & number container----------------------------')
#             print(contains_non_alpha_num)
#             if contains_non_alpha_num != None:
#                 print('===============yes contains non alpha & digit---------------------')

#                 unwanted_characterz = ['~', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#                                        '_', '-', '+', '=', '[', ']', '{', '}', '|', '', ":",
#                                        ";", '"', "'", '<', ",", '>', ".", "/", "?"]
#                 contain_unwanted_characterz = False

#                 contains_the_required_chars = re.search(r"[-_/]", stri2)
#                 print(f'chars_container is ({contains_the_required_chars})')
#                 for i in stri2:
#                     if i in unwanted_characterz:
#                         print('===============it contains the required char---------------------')
#                         contain_unwanted_characterz = True
#                         return JsonResponse({'exists': it_exists})
#                     break
#                 if contains_the_required_chars != None and not contain_unwanted_characterz:
#                     print('===============it contains the required char---------------------')
#                     return JsonResponse({'exists': it_exists})
#         else:
#             return JsonResponse({'exists': it_exists})

#         response = JsonResponse({'exists': it_exists})
#     if request.GET.get('action') == 'check_password2':
#         it_exists = UserBase.objects.filter(password2__exact=content).exists()
#         response = JsonResponse({'exists': it_exists})
#         char = ["/", '.', '-', '_']
#         num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#     return response

# def registration_check(request):
#     content = request.GET.get('content')
#     if request.GET.get('action') == 'check_username':
#         it_exists = UserBase.objects.filter(user_name__exact=content).exists()
#         contains_characters = re.search(r"\W", content)
#         if not it_exists:
#             if len(content) >= 4:
#                 if contains_characters != None:
#                     return JsonResponse({'msg_type':False, 'msg': 'Username must not include characters'})
#                 else:
#                     return JsonResponse({'msg_type': True, 'msg': ''})
#             else:
#                 return JsonResponse({'msg_type': False, 'msg': 'Username must be 4 or more characters'})
#         else:
#             return JsonResponse({'msg_type':False, 'msg': 'Username is already in use'})


#     contain_unwanted_characterz = False
#     if request.GET.get('action') == 'check_email':
#         it_exists = UserBase.objects.filter(email__exact=content).exists()
#         if not it_exists:
#             contain_unwanted_characterz =False
#             #checks & executes if it contains characters
#             contains_non_characters = re.search(r"\W", content)
#             if contains_non_characters != None:
#                 unwanted_characterz = ['~', '!', '#', '$', '%', '^', '&', '*', '(', ')', \
#                              '+', '=', '[', ']', '{', '}', '|', '', ":", ";", '"', "'", \
#                                '<', ",", '>', "?"]

#                 for i in content:
#                     if i in unwanted_characterz:
#                         contain_unwanted_characterz =True
#                         break
#             if contain_unwanted_characterz == True:
#                 return JsonResponse({'msg_type':False, 'msg': 'Email contain unwanted character'})

#             # checks & executes if it doesnt contains characters at all / bad character
#             elif contain_unwanted_characterz == False:
#                 ends_with = re.search(r'@yahoo.com$|gmail.com$|hotmail.com$', content)
#                 if ends_with != None:
#                     return JsonResponse({'msg_type':True, 'msg': ''})
#                 else:
#                     return JsonResponse({'msg_type':False, 'msg': "Email end contains wrong pattern, use ('gmail.com' etc)"})

#         else:
#             return JsonResponse({'msg_type':False, 'msg': 'Email is already in use'})


#     if request.GET.get('action') == 'check_password':
#         it_exists = UserBase.objects.filter(password__exact=content).exists()
#         contains_characters = re.search(r"\W", content)
#         contains_digit = re.search(r"\d", content)
#         contains_white_space = re.search(r"\s", content)
#         if len(content) >= 8:
#             if contains_characters == None:
#                 return JsonResponse({'msg_type':False, 'msg': 'Password must include characters'})
#             if contains_digit != None:
#                 print('cyyyyyyyyyyyyyyyyyyyyyyy')
#             if contains_digit == None:
#                 return JsonResponse({'msg_type':False, 'msg': 'Password must include digits'})
#             if contains_white_space != None:
#                 return JsonResponse({'msg_type':False, 'msg': 'Password allows no white space'})
#             else:
#                 return JsonResponse({'msg_type':True, 'msg': ''})
#         else:
#             return JsonResponse({'msg_type':False,'msg': 'password must be longer than 8 characters'})
#     if request.GET.get('action') == 'check_password2':
#         it_exists = UserBase.objects.filter(password2__exact=content).exists()
#         response = JsonResponse({'exists': it_exists})
#         char = ["/",'.','-','_']
#         num = [1,2,3,4,5,6,7,8,9,0]

#     return JsonResponse({'exists': it_exists})


@login_required
def dashboard(request):
    pass
