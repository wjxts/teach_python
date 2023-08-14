refer [gpt](https://chat.openai.com/share/59cfc668-10ac-4e39-98dd-a46950438e5e)
``` bash
vim .vimrc
```
写入
``` bash
" 基本设置
set nocompatible       " 不使用 vi 兼容模式
set number             " 显示行号
set autoindent         " 自动缩进
set expandtab          " 使用空格代替制表符
set tabstop=4          " 制表符宽度为 4
set softtabstop=4      " 缩进宽度为 4
set shiftwidth=4       " 自动缩进宽度为 4
set smartindent        " 智能缩进

" 高亮搜索结果
set hlsearch           " 高亮搜索结果
set incsearch          " 实时显示搜索匹配

" 颜色设置
syntax enable          " 启用语法高亮
set background=dark   " 暗色主题背景

" 撤销历史
set undofile           " 持久化撤销历史

" 插件管理器（vim-plug）
call plug#begin('~/.vim/plugged')
Plug 'tpope/vim-fugitive'   " Git 集成
Plug 'vim-airline/vim-airline'  " 状态栏美化
Plug 'scrooloose/nerdtree'  " 文件浏览器
Plug 'preservim/nerdcommenter'  " 快速注释插件
call plug#end()

" 插件配置
" Airline 配置
" let g:airline_theme='gruvbox'

" NERDTree 配置
map <C-n> :NERDTreeToggle<CR>
let g:NERDTreeWinPos = "left"

" NERDCommenter 配置
let g:NERDSpaceDelims=1  " 在注释中添加空格
let g:NERDCompactSexyComs=1  " 使用紧凑的注释样式

" 自动保存文件
autocmd BufWritePre * :%s/\s\+$//e

" 其他设置
set mouse=a          " 启用鼠标支持
set wildmenu         " 启用命令行模式下的补全
set clipboard=unnamedplus  " 支持与系统剪贴板交互

" 映射快捷键
map <leader>ev :vsplit $MYVIMRC<CR>  " 编辑 .vimrc 文件
```

Install plugin

```bash
:PlugInstall
```
maybe need
```bash
:PlugClean
```
切换到某一行
```bash
:行号
```
切换到首行: gg, 切换到最后一行:shift+g

粘贴到这一行的下一行: p
回撤: u
复制1行: yy
复制多行: (1) 在复制的起始行按v，然后移动到最后一行按y (2):5,10y 从5到10行
移到行末的非空字符: g_, 移到行首的非空字符^

代码补全见gpt, coc.nvim node.js使用conda安装  
coc.nvim初步使起来不太习惯