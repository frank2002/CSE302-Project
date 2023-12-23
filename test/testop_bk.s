	.text
	.globl	test
test:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$208, %rsp
	movq	%rdi, -8(%rbp)
.L24:
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$20, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$2, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	$0, -56(%rbp)
	movq	-56(%rbp), %r11
	movq	%r11, -64(%rbp)
	movq	$0, -72(%rbp)
	movq	-72(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	$0, -88(%rbp)
	movq	-88(%rbp), %r11
	movq	%r11, -96(%rbp)
	movq	$0, -104(%rbp)
	movq	-104(%rbp), %r11
	movq	%r11, -112(%rbp)
	movq	$0, -120(%rbp)
	movq	-120(%rbp), %r11
	movq	%r11, -128(%rbp)
	movq	-16(%rbp), %rax
	cqto
	idivq	-32(%rbp)
	movq	%rax, -136(%rbp)
	movq	-136(%rbp), %r11
	movq	%r11, -144(%rbp)
	movq	-16(%rbp), %rax
	cqto
	idivq	-32(%rbp)
	movq	%rdx, -152(%rbp)
	movq	-152(%rbp), %r11
	movq	%r11, -160(%rbp)
	movq	-16(%rbp), %rax
	imulq	-32(%rbp)
	movq	%rax, -168(%rbp)
	movq	-168(%rbp), %r11
	movq	%r11, -176(%rbp)
	movq	-16(%rbp), %r11
	movq	-48(%rbp), %rcx
	sarq	%cl, %r11
	movq	%r11, -184(%rbp)
	movq	-184(%rbp), %r11
	movq	%r11, -192(%rbp)
	movq	-16(%rbp), %r11
	movq	-48(%rbp), %rcx
	salq	%cl, %r11
	movq	%r11, -200(%rbp)
	movq	-200(%rbp), %r11
	movq	%r11, -208(%rbp)
	movq	-144(%rbp), %rax
	jmp	.E_test
.E_test:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$48, %rsp
.L25:
	movq	$0, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$50, -24(%rbp)
	movq	-24(%rbp), %rdi
	callq	test
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
