from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'grades.tests.test_course_grade')

from lms.djangoapps.grades.tests.test_course_grade import *
