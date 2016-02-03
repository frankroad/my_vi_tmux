set nocompatible
set background=dark
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'L9'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'klen/python-mode'
Plugin 'tomasr/molokai'
Plugin 'ervandew/supertab'
call vundle#end()
filetype plugin indent on

:set tabstop=4
:set shiftwidth=4
:set expandtab
:set encoding=utf-8
set pastetoggle=<F3>
set number
