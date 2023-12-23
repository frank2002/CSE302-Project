	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$248, %rsp
.L44:
	movq	$833779, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$2, -24(%rbp)
	pushq	%rdx
	movq	-16(%rbp), %rax
	cqto
	idivq	-24(%rbp)
	movq	%rdx, -32(%rbp)
	popq	%rdx
	movq	$0, -40(%rbp)
	movq	-40(%rbp), %r11
	subq	-32(%rbp), %r11
	movq	%r11, -48(%rbp)
	cmpq	$0, -48(%rbp)
	jz	.L2
.L45:
.L3:
	movq	$3, -56(%rbp)
	pushq	%rdx
	movq	-16(%rbp), %rax
	cqto
	idivq	-56(%rbp)
	movq	%rdx, -64(%rbp)
	popq	%rdx
	movq	$0, -72(%rbp)
	movq	-72(%rbp), %r11
	subq	-64(%rbp), %r11
	movq	%r11, -80(%rbp)
	cmpq	$0, -80(%rbp)
	jz	.L10
.L46:
.L11:
	movq	$5, -88(%rbp)
	pushq	%rdx
	movq	-16(%rbp), %rax
	cqto
	idivq	-88(%rbp)
	movq	%rdx, -96(%rbp)
	popq	%rdx
	movq	$0, -104(%rbp)
	movq	-104(%rbp), %r11
	subq	-96(%rbp), %r11
	movq	%r11, -112(%rbp)
	cmpq	$0, -112(%rbp)
	jz	.L18
.L47:
.L19:
	movq	$7, -120(%rbp)
	pushq	%rdx
	movq	-16(%rbp), %rax
	cqto
	idivq	-120(%rbp)
	movq	%rdx, -128(%rbp)
	popq	%rdx
	movq	$0, -136(%rbp)
	movq	-136(%rbp), %r11
	subq	-128(%rbp), %r11
	movq	%r11, -144(%rbp)
	cmpq	$0, -144(%rbp)
	jz	.L26
.L48:
.L27:
	movq	$11, -152(%rbp)
	pushq	%rdx
	movq	-16(%rbp), %rax
	cqto
	idivq	-152(%rbp)
	movq	%rdx, -160(%rbp)
	popq	%rdx
	movq	$0, -168(%rbp)
	movq	-168(%rbp), %r11
	subq	-160(%rbp), %r11
	movq	%r11, -176(%rbp)
	cmpq	$0, -176(%rbp)
	jz	.L34
.L49:
.L35:
	movq	$0, -184(%rbp)
	movq	-184(%rbp), %rdi
	callq	print_int
.L36:
.L28:
.L20:
.L12:
.L4:
	movq	$0, -192(%rbp)
	movq	-192(%rbp), %rax
	jmp	.E_main
.L34:
	movq	$11, -200(%rbp)
	movq	-200(%rbp), %rdi
	callq	print_int
	jmp	.L36
.L26:
	movq	$7, -208(%rbp)
	movq	-208(%rbp), %rdi
	callq	print_int
	jmp	.L28
.L18:
	movq	$5, -216(%rbp)
	movq	-216(%rbp), %rdi
	callq	print_int
	jmp	.L20
.L10:
	movq	$3, -224(%rbp)
	movq	-224(%rbp), %rdi
	callq	print_int
	jmp	.L12
.L2:
	movq	$2, -232(%rbp)
	movq	-232(%rbp), %rdi
	callq	print_int
	jmp	.L4
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
