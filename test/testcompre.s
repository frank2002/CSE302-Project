	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$152, %rsp
.L29:
	movq	$20, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$0, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$0, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
.L6:
.L7:
	movq	$0, -56(%rbp)
	movq	-56(%rbp), %r11
	subq	-16(%rbp), %r11
	movq	%r11, -64(%rbp)
	cmpq	$0, -64(%rbp)
	jz	.L9
.L30:
.L10:
.L11:
	movq	-16(%rbp), %rdi
	callq	print_int
	movq	$1, -72(%rbp)
	movq	-72(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$0, -80(%rbp)
	movq	-80(%rbp), %r11
	movq	%r11, -48(%rbp)
.L16:
.L17:
	movq	-16(%rbp), %r11
	subq	-32(%rbp), %r11
	movq	%r11, -88(%rbp)
	cmpq	$0, -88(%rbp)
	jl	.L19
.L32:
.L20:
.L21:
	movq	-48(%rbp), %r11
	addq	-32(%rbp), %r11
	movq	%r11, -96(%rbp)
	movq	-96(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	$1, -104(%rbp)
	movq	-32(%rbp), %r11
	addq	-104(%rbp), %r11
	movq	%r11, -112(%rbp)
	movq	-112(%rbp), %r11
	movq	%r11, -32(%rbp)
	jmp	.L16
.L19:
.L18:
	movq	-48(%rbp), %rdi
	callq	print_int
	movq	$1, -120(%rbp)
	movq	-16(%rbp), %r11
	subq	-120(%rbp), %r11
	movq	%r11, -128(%rbp)
	movq	-128(%rbp), %r11
	movq	%r11, -16(%rbp)
	jmp	.L6
.L9:
.L8:
	movq	$0, -136(%rbp)
	movq	-136(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
