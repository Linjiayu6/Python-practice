
# -*- coding: utf-8 -*

import os
# posix, 如果是posix，说明系统是Linux、Unix或Mac OS X
print os.name

# 详情
# ('Darwin', 'linjiayudeMacBook-Pro.local', '17.7.0', 'Darwin Kernel Version 17.7.0: Wed Apr 24 21:17:24 PDT 2019; root:xnu-4570.71.45~1/RELEASE_X86_64', 'x86_64')
print os.uname()

# 环境变量
"""
{'LESS': '-R', 'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'LC_TERMINAL_VERSION': '3.3.0beta13', 'LC_CTYPE': 'en_GB.UTF-8', 'TERM_PROGRAM_VERSION': '3.3.0beta13', 'LOGNAME': 'linjiayu', 'USER': 'linjiayu', 'NVM_DIR': '/Users/linjiayu/.nvm', 'PATH': '/Users/linjiayu/pay/flutter/flutter_bash_profile/bin:/Users/linjiayu/.yarn/bin:/usr/local/bin:/Users/linjiayu/.nvm/versions/node/v10.0.0/bin:/Users/linjiayu/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin', 'HOME': '/Users/linjiayu', 'NVM_IOJS_ORG_MIRROR': 'https://iojs.org/dist', 'ZSH': '/Users/linjiayu/.oh-my-zsh', 'TERM_PROGRAM': 'iTerm.app', 'LANG': 'en_GB.UTF-8', 'LC_TERMINAL': 'iTerm2', 'TERM': 'xterm-256color', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.Ms3SOTx995/Render', 'COLORFGBG': '7;0', 'NVM_IOJS_ORG_VERSION_LISTING': 'https://iojs.org/dist/index.tab', 'SHLVL': '1', 'XPC_FLAGS': '0x0', 'NVM_BIN': '/Users/linjiayu/.nvm/versions/node/v10.0.0/bin', 'NVM_PATH': '/Users/linjiayu/.nvm/versions/node/v10.0.0/lib/node', 'ITERM_SESSION_ID': 'w0t0p0:79F010EA-D753-45B2-94AF-0B4EF090EB9B', '_': '/usr/bin/python', 'MANPATH': '/Users/linjiayu/.nvm/versions/node/v10.0.0/share/man:/usr/local/share/man:/usr/share/man:/Applications/Xcode.app/Contents/Developer/usr/share/man:/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/man', 'SDKMAN_VERSION': '5.7.3+337', 'SDKMAN_CANDIDATES_DIR': '/Users/linjiayu/.sdkman/candidates', 'TERM_SESSION_ID': 'w0t0p0:79F010EA-D753-45B2-94AF-0B4EF090EB9B', 'XPC_SERVICE_NAME': '0', 'SDKMAN_CANDIDATES_API': 'https://api.sdkman.io/2', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.VrakTtk9HA/Listeners', 'SDKMAN_DIR': '/Users/linjiayu/.sdkman', 'SHELL': '/bin/zsh', 'ITERM_PROFILE': 'Default', 'TMPDIR': '/var/folders/nx/x51_x03x39jcd4k332nbzw8r0000gn/T/', 'SDKMAN_PLATFORM': 'Darwin', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'OLDPWD': '/Users/linjiayu/LinProject/Spider-python/pythonNote/0805_IO', 'VERSIONER_PYTHON_VERSION': '2.7', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x2', 'PWD': '/Users/linjiayu/LinProject/Spider-python/pythonNote/0805_IO/os', 'COLORTERM': 'truecolor', 'PAGER': 'less', 'NVM_NODEJS_ORG_MIRROR': 'https://nodejs.org/dist'}
"""
print os.environ

"""
/Users/linjiayu/pay/flutter/flutter_bash_profile/bin:/Users/linjiayu/.yarn/bin:/usr/local/bin:/Users/linjiayu/.nvm/versions/node/v10.0.0/bin:/Users/linjiayu/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
"""
print os.getenv('PATH')