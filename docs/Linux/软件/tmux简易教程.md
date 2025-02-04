
Tmux是一个终端复用器（terminal multiplexer）

帮助命令的快捷键是 `Ctrl+b ?`：在 Tmux 窗口中，先按下 `Ctrl+b`，再按下 `?`，就会显示帮助信息

然后，按下 ESC 键或`q`键，就可以退出帮助

## 会话

命令行的典型用法是打开终端（terminal）后，在里面输入指令。用户的这种与计算机交互的手段，称为**会话**（session）。

在会话中，通过命令行启动的所有进程均与会话进程绑定。当会话进程终止时，该会话启动的所有进程也会随之强行结束。

一点最常见的例子就是通过SSH连接到远程计算机。当SSH连接因为网络等原因断开时，那么SSH会话就被终止，这次会话启动的任务也会被强制结束。

为了解决这个问题，一种手段就是用户终端窗口与会话“解绑”。即**关闭用户端窗口，仍然维持该会话**，进而保证用户进程不变。

## Tmux 作用

1. 它允许在单个窗口中，同时访问多个会话。这对于同时运行多个命令行程序很有用。
2. 它可以让新窗口"接入"已经存在的会话。
3. 它允许每个会话有多个连接窗口，因此可以多人实时共享会话。
4. 它还支持窗口任意的垂直和水平拆分

简而言之，Tmux 实现了窗口和会话的解绑

## Tmux 使用

进入 Tmux 窗口： `tmux`

退出 Tmux 窗口：`exit` 或 `Ctrl+d`

### 会话相关

新建命名会话：`tmux new -s <session-name>`

分离会话：`tmux detach` 或 `Ctrl+b+d`

> [!important]-
> 
> 分离会话会退出当前窗口，但会话和里面的进程仍然在后台运行

接入会话：`tmux attach -t <session-name>`

杀死会话：`tmux kill-session -t <session-name>`

切换会话：`tmux switch -t <session-name>`

重命名会话：`tmux rename-session -t <old-session-name> <new-name>` 或 `Ctrl+b+$`

查看当前所有会话：`tmux ls` 或 `Ctrl+b+s`

### 窗格相关  

Tmux 可以将窗口分成多个窗格（pane），每个窗格运行不同的命令

划分窗口为上下：`tmux split-window` 或 `Ctrl+b+"`

划分窗口为左右：`tmux split-window -h` 或 `Ctrl+b+%`

移动光标到上侧窗格：`tmux select-pane -U` 或 `Ctrl+b+↑`

移动光标到下侧窗格：`tmux select-pane -D` 或 `Ctrl+b+↓`

移动光标到左侧窗格：`tmux select-pane -L` 或 `Ctrl+b+←`

移动光标到右侧窗格：`tmux select-pane -R` 或 `Ctrl+b+→`

将当前窗格上移：`tmux swap-pane -U`

将当前窗格下移：`tmux swap-pane -D`

### 窗口相关

新建窗口：`tmux new-window` 或 `Ctrl+b+c`

新建命名窗口：`tmux new-window -n <window-name>`    

切换到指定编号窗口：`tmux select-window -t <window-number>`

切换到指定名称窗口：`tmux select-window -t <window-name>`

重命名窗口：`tmux rename-window <new-name>`

### 查看命令相关

列出所有快捷键，及其对应的 Tmux 命令：`tmux list-keys`

列出所有 Tmux 命令及其参数：`tmux list-commands`

列出当前所有 Tmux 会话信息：`tmux info` 

## 实例



## 参考

1. [Tmux 使用教程](https://www.ruanyifeng.com/blog/2019/10/tmux.html)
