.model small
.stack 100h

.data
msg     db 'Binary of 13 is: $'
newline db 13, 10, '$'

.code
main:
    mov ax, @data
    mov ds, ax

    ; Show message
    lea dx, msg
    mov ah, 09h
    int 21h
    
    ; Convert decimal 13 to binary using stack
    mov ax, 13        ; Number to convert
    xor cx, cx        ; Bit counter = 0

convert_loop:
    xor dx, dx        ; Clear remainder
    mov bx, 2
    div bx            ; AX / 2 → Quotient in AX, Remainder in DX

    push dx           ; Save remainder (0 or 1)
    inc cx            ; Count how many bits pushed

    cmp ax, 0
    jne convert_loop  ; Continue until quotient is 0

    ; Newline
    lea dx, newline
    mov ah, 09h
    int 21h

print_binary:
    pop dx
    add dl, '0'       ; Convert 0/1 to ASCII
    mov ah, 02h
    int 21h

    loop print_binary ; Loop until CX = 0

    ; Exit to DOS
    mov ah, 4Ch
    int 21h
end main
