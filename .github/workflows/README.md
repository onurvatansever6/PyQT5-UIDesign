"on:" -> When do I execute this commands.

"runs-on:" -> This determines what platform Github-Actions is using for executing your commands.

"name:" -> You can name your actions with this command. Name will be shown on Github-Actions steps.

"run:" -> This command runs your scripts on current Github-Actions VM's terminal.

"env:" -> In this section you can specify environment variables for your tests to run.

Needed dependencies for QT tests to run: 

sudo apt install libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 x11-utils
        /sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -screen 0 1920x1200x24 -ac +extension GLX
        python -m pip install --upgrade pip
        pip install pyside2 pytest coverage pytest-qt pyqt5-tools

Commands for running pytest:

ulimit -c unlimited
        xvfb-run -a pytest

Environment variables for QT tests:
        DISPLAY: ':99.0'
        QT_DEBUG_PLUGINS: 1