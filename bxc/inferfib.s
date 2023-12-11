	.text
	.globl	fib
fib:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	%rdi, %rcx
.L21:
	movq	%rcx, %r11
	movq	%r11, %rax
	movq	$20, %rcx
	movq	%rcx, %r11
	movq	%r11, %rcx
	movq	%rax, %r11
	movq	%r11, %rcx
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, %r8
	movq	$1, %rax
	movq	%rax, %r11
	movq	%r11, %r9
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, %rax
	movq	%rcx, %r11
	movq	%r11, %rsi
	movq	%r8, %r11
	movq	%r11, %rax
	movq	%r9, %r11
	movq	%r11, %rdx
.L8:
	movq	$0, %rdi
	movq	%rdi, %r11
	subq	%rsi, %r11
	movq	%r11, %rdi
	cmpq	$0, %rdi
	jl	.L9
.L22:
.L10:
	movq	%rax, %rax
	jmp	.E_fib
.L9:
	movq	$1, %rdi
	movq	%rsi, %r11
	subq	%rdi, %r11
	movq	%r11, %rdi
	movq	%rdi, %r11
	movq	%r11, %rsi
	movq	%rax, %r11
	addq	%rdx, %r11
	movq	%r11, %rdi
	movq	%rdi, %r11
	movq	%r11, %rax
	movq	%rdx, %r11
	movq	%r11, %rdi
	movq	%rax, %r11
	movq	%r11, %rdx
	movq	%rsi, %r11
	movq	%r11, %rsi
	movq	%rdi, %r11
	movq	%r11, %rax
	movq	%rdx, %r11
	movq	%r11, %rdx
	jmp	.L8
.E_fib:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$56, %rsp
.L23:
	movq	$0, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$50, -24(%rbp)
	movq	-24(%rbp), %rdi
	callq	fib
	movq	%rax, -32(%rbp)
	movq	-32(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	-16(%rbp), %rdi
	callq	print_int
	movq	$0, -40(%rbp)
	movq	-40(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
