#-*- coding: utf-8 -*-
u'''
MOD 11: common Java developers errors
'''


#===============================================================================
# - Getters and setters are not needed
#    - There is always direct attribute access
#    - Use properties or decorators if you really need to intercept attribute access
#===============================================================================


#===============================================================================
# - Abuse of @staticmethod and @classmethod
#    - @staticmethod has no sense. Only justification is organization of code
#        - You can define functions and attributes directly in modules
#    - @classmethod only used in constructors. Try to avoid class methods and attributes
#===============================================================================


#===============================================================================
# - Define only one class per module
#    - You can define several "helper" or internal classes in the same module
#        - And even functions and attributes
#===============================================================================


#===============================================================================
# - Fear to multiple inheritance
#    - Mixins and multiple inheritance are widely used in Python
#    - You must understand what you are implementing, that's your work
#    - "we're all grown-ups here"
#===============================================================================


#===============================================================================
# - Abuse of type checking
#    - Duck typing and EAFP (It is Easier to Ask for Forgiveness than Permission)
#    - Get used to the "uncertainity" of the exact type of your arguments
#===============================================================================


#===============================================================================
# - Don't forget the Zen of Python
#===============================================================================

import this
