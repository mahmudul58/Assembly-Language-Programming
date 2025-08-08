.model small
.stack 100h
.data
msg       db 'Enter a line: $'
countMsg  db 'Total characters: $'
.code
main proc
   mov ax,@data
   mov ds,ax

   ; prompt
   mov ah,9
   lea dx,msg
   int 21h

   xor cx,cx         ; counter = 0

read_loop:
   mov ah,1
   int 21h
   cmp al,13
   je done_reading
   inc cx
   jmp read_loop

done_reading:
   ; show message
   mov ah,9
   lea dx,countMsg
   int 21h

   ; convert CX to decimal (supports up to 2 digits here)
   mov ax,cx
   mov bl,10
   xor dx,dx
   div bl            ; AL = tens, AH = units
   mov bh,ah         ; save units in BH BEFORE any int 21h (AH will be clobbered)

   ; print tens
   add al,'0'
   mov dl,al
   mov ah,2
   int 21h

   ; print units from BH
   mov dl,bh
   add dl,'0'
   mov ah,2
   int 21h

   ; exit
   mov ah,4Ch
   int 21h
main endp
end main
