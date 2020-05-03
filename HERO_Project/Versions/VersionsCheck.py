from HERO_Project.Versions.LinuxVersions import LinuxVersions


class VersionsCheck(object):

    @classmethod
    def getVersion(cls, linuxVersion, versionInput):
        ver = "Kernel version: "
        version = set(
            map(lambda l: (l[len(ver):].split('\n')[0]), filter(lambda line: line.startswith(ver), linuxVersion)))
        count = 1

        linuxvers = LinuxVersions.versionsOfCentOs()
        for getVer in version:
            fil = list(filter(lambda line: getVer.startswith(line), linuxvers))[0]
            if linuxvers.index(fil) >= linuxvers.index(versionInput):
                count = 0

        return count
