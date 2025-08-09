.model small
.stack 100h
.data
msg1 db 10,13,'ENTER A HEX DIGIT:$'
msg2 db 10,13,'IN DECIMAL IS IT:$'
msg3 db 10,13,'DO YOU WANT TO DO IT AGAIN?$'
msg4 db 10,13,'ILLEGAL CHARACTER- ENTER 0-9 OR A-F:$'

newl db 13,10,'$'
.code
main proc
    mov ax,@data
    mov ds,ax

loop_:
    lea dx,msg1
    mov ah,9
    int 21h
go:
    mov ah,1
    int 21h
    mov bl,al

    cmp bl,'9'
    jle num

hex:
    cmp bl,'A'
    jl illigal
    cmp bl,'F'
    ja illigal

    mov ah,9
    lea dx,msg2
    int 21h

    mov ah,2
    mov dl,'1'
    int 21h

    mov dl,bl
    sub dl,17
    int 21h
    jmp again
    
illigal:
    mov ah,9
    lea dx,msg4
    int 21h
    jmp go
num:
    cmp bl,'0'
    jb illigal
    mov ah,9
    lea dx,msg2
    int 21h

    mov ah,2
    mov dl,bl
    int 21h
    jmp again

again:
    mov ah,9
    lea dx,msg3
    int 21h
    mov ah,1
    int 21h
    cmp al,'y'
    je loop_
    cmp al,'Y'
    je loop_

exit:
    mov ah,4Ch
    int 21h
    main endp
    end main
