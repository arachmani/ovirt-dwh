#
# ovirt-engine-setup -- ovirt engine setup
# Copyright (C) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""Constants."""


import os
import gettext
_ = lambda m: gettext.dgettext(message=m, domain='ovirt-engine-dwh')


from otopi import util


from constants import classproperty, osetupattrsclass, osetupattrs


from . import dwhconfig


@util.export
@util.codegen
class Const(object):
    PACKAGE_NAME = dwhconfig.PACKAGE_NAME
    PACKAGE_VERSION = dwhconfig.PACKAGE_VERSION
    DISPLAY_VERSION = dwhconfig.DISPLAY_VERSION
    RPM_VERSION = dwhconfig.RPM_VERSION
    RPM_RELEASE = dwhconfig.RPM_RELEASE
    SERVICE_NAME = 'ovirt-engine-dwhd'
    OVIRT_ENGINE_DWH_DB_BACKUP_PREFIX = 'dwh'
    OVIRT_ENGINE_DWH_PACKAGE_NAME = 'ovirt-engine-dwh'
    OVIRT_ENGINE_DWH_SETUP_PACKAGE_NAME = 'ovirt-engine-dwh-setup'

    @classproperty
    def DWH_DB_ENV_KEYS(self):
        return {
            'host': DBEnv.HOST,
            'port': DBEnv.PORT,
            'secured': DBEnv.SECURED,
            'hostValidation': DBEnv.SECURED_HOST_VALIDATION,
            'user': DBEnv.USER,
            'password': DBEnv.PASSWORD,
            'database': DBEnv.DATABASE,
            'connection': DBEnv.CONNECTION,
            'pgpassfile': DBEnv.PGPASS_FILE,
        }


@util.export
@util.codegen
class Defaults(object):
    DEFAULT_DB_HOST = 'localhost'
    DEFAULT_DB_PORT = 5432
    DEFAULT_DB_DATABASE = 'ovirt_engine_history'
    DEFAULT_DB_USER = 'ovirt_engine_history'
    DEFAULT_DB_PASSWORD = ''
    DEFAULT_DB_SECURED = False
    DEFAULT_DB_SECURED_HOST_VALIDATION = False


@util.export
@util.codegen
class FileLocations(object):
    PKG_SYSCONF_DIR = dwhconfig.PKG_SYSCONF_DIR
    PKG_STATE_DIR = dwhconfig.PKG_STATE_DIR
    PKG_DATA_DIR = dwhconfig.PKG_DATA_DIR
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG = \
        dwhconfig.OVIRT_ENGINE_DWHD_SERVICE_CONFIG
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DEFAULTS = \
        dwhconfig.OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DEFAULTS
    OVIRT_ENGINE_DWHD_SERVICE_CONFIGD = '%s.d' % \
        OVIRT_ENGINE_DWHD_SERVICE_CONFIG
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DATABASE = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '10-setup-database.conf',
    )
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_JBOSS = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '10-setup-jboss.conf',
    )
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_LEGACY = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '20-setup-legacy.conf',
    )
    OVIRT_ENGINE_DWH_DB_DIR = os.path.join(
        PKG_DATA_DIR,
        'dbscripts',
    )
    OVIRT_ENGINE_DWH_DB_CREATE = os.path.join(
        OVIRT_ENGINE_DWH_DB_DIR,
        'create_schema.sh',
    )
    OVIRT_ENGINE_DWH_DB_UPGRADE = os.path.join(
        OVIRT_ENGINE_DWH_DB_DIR,
        'upgrade.sh',
    )
    OVIRT_ENGINE_DWH_DB_BACKUP_DIR = os.path.join(
        PKG_STATE_DIR,
        'backups',
    )
    LEGACY_CONFIG = os.path.join(
        PKG_SYSCONF_DIR,
        '..',
        'ovirt-engine',
        'ovirt-engine-dwh',
        'Default.properties',
    )


@util.export
class Stages(object):
    CORE_ENABLE = 'osetup.dwh.core.enable'
    DB_CONNECTION_SETUP = 'osetup.dwh.db.connection.setup'
    DB_CREDENTIALS_AVAILABLE = 'osetup.dwh.db.connection.credentials'
    DB_CONNECTION_CUSTOMIZATION = 'osetup.dwh.db.connection.customization'
    DB_CONNECTION_AVAILABLE = 'osetup.dwh.db.connection.available'
    DB_SCHEMA = 'osetup.dwh.db.schema'


@util.export
@util.codegen
@osetupattrsclass
class CoreEnv(object):

    @osetupattrs(
        answerfile=True,
        postinstallfile=True,
        summary=True,
        description=_('DWH installation'),
    )
    def ENABLE(self):
        return 'OVESETUP_DWH_CORE/enable'


@util.export
@util.codegen
@osetupattrsclass
class DBEnv(object):

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database host'),
    )
    def HOST(self):
        return 'OVESETUP_DWH_DB/host'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database port'),
    )
    def PORT(self):
        return 'OVESETUP_DWH_DB/port'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database secured connection'),
    )
    def SECURED(self):
        return 'OVESETUP_DWH_DB/secured'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database host name validation'),
    )
    def SECURED_HOST_VALIDATION(self):
        return 'OVESETUP_DWH_DB/securedHostValidation'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database name'),
    )
    def DATABASE(self):
        return 'OVESETUP_DWH_DB/database'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database user name'),
    )
    def USER(self):
        return 'OVESETUP_DWH_DB/user'

    @osetupattrs(
        answerfile=True,
    )
    def PASSWORD(self):
        return 'OVESETUP_DWH_DB/password'

    CONNECTION = 'OVESETUP_DWH_DB/connection'
    STATEMENT = 'OVESETUP_DWH_DB/statement'
    PGPASS_FILE = 'OVESETUP_DWH_DB/pgPassFile'
    NEW_DATABASE = 'OVESETUP_DWH_DB/newDatabase'


@util.export
@util.codegen
@osetupattrsclass
class RemoveEnv(object):
    @osetupattrs(
        answerfile=True,
    )
    def REMOVE_DATABASE(self):
        return 'OVESETUP_DWH_REMOVE/database'


@util.export
@util.codegen
@osetupattrsclass
class ProvisioningEnv(object):

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('Configure local DWH database'),
    )
    def POSTGRES_PROVISIONING_ENABLED(self):
        return 'OVESETUP_DWH_PROVISIONING/postgresProvisioningEnabled'


# vim: expandtab tabstop=4 shiftwidth=4
