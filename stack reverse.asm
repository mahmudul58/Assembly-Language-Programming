.model small
.stack 100h
.data
.code
main proc
   mov cx,0
   mov ah,1

input_loop:
   cmp al,13
   je end_loop
   push ax
   inc cx
   int 21h
   jmp input_loop

end_loop:
   jcxz exit

   mov ah,2
print:
   pop dx
   int 21h
   loop print
  
exit:
   mov ah,4Ch
   int 21h
   main endp
   end main
