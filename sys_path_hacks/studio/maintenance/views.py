from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'maintenance.views')

from cms.djangoapps.maintenance.views import *
