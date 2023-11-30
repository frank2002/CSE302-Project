	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$64, %rsp
.L7:
	movq	$10, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$20, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	-32(%rbp), %rdi
	callq	print_int
	movq	$1, -40(%rbp)
	movq	-32(%rbp), %r11
	addq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	-48(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	-16(%rbp), %rdi
	callq	print_int
	movq	$0, -56(%rbp)
	movq	-56(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
