"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.conf import settings as django_settings
from core.utils.common import collect_versions
from core.feature_flags import all_flags


def sentry_fe(request):
    # return the value you want as a dictionary, you may add multiple values in there
    return {
        'SENTRY_FE': django_settings.SENTRY_FE
    }


def settings(request):
    """ Make available django settings on each template page
    """
    versions = collect_versions()

    # django templates can't access names with hyphens
    versions['lsf'] = versions.get('singularity-loop-frontend', {})
    versions['lsf']['commit'] = versions['lsf'].get('commit', 'none')[0:6]

    versions['backend'] = {}
    if 'singularity-loop-os-backend' in versions:
        versions['backend']['commit'] = versions['singularity-loop-os-backend'].get('commit', 'none')[0:6]
    if 'singularity-loop-enterprise-backend' in versions:
        versions['backend']['commit'] = versions['singularity-loop-enterprise-backend'].get('commit', 'none')[0:6]

    if 'dm2' in versions:
        versions['dm2']['commit'] = versions['dm2'].get('commit', 'none')[0:6]

    feature_flags = {}
    if hasattr(request, 'user'):
        feature_flags = all_flags(request.user)

    return {
        'settings': django_settings,
        'versions': versions,
        'feature_flags': feature_flags
    }
