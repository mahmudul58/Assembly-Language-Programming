.model small
.stack 100h

.data
arr db 5 dup(?)  ; Array to store 5 characters
len equ 5
msg db 'Enter 5 characters: $'
newline db 13, 10, '$'

.code
main proc
    mov ax, @data
    mov ds, ax

    ; Display prompt
    mov ah, 09h
    lea dx, msg
    int 21h

    ; Read 5 characters, store in arr, push to stack
    mov cx, len
    mov si, 0

input_loop:
    mov ah, 01h       ; Read character with echo
    int 21h
    mov arr[si], al   ; Store in array
    push ax           ; Push onto stack
    inc si
    loop input_loop

    ; Reverse: pop from stack into array
    mov cx, len
    mov si, 0

reverse_loop:
    pop ax
    mov arr[si], al
    inc si
    loop reverse_loop

    ; Newline
    mov ah, 09h
    lea dx, newline
    int 21h

    ; Display reversed characters
    mov cx, len
    mov si, 0

display_loop:
mov ah, 02h
    mov dl, arr[si]
    
    int 21h
    inc si
    loop display_loop

    ; Exit to DOS
    exit:
    mov ah, 4Ch
    int 21h
    main endp
    end main
