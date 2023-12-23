	.text
	.globl	compute
compute:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$184, %rsp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
.L38:
	movq	$0, -32(%rbp)
	movq	-32(%rbp), %r11
	subq	-8(%rbp), %r11
	movq	%r11, -40(%rbp)
	cmpq	$0, -40(%rbp)
	jge	.L0
.L39:
.L1:
.L2:
	movq	$0, -48(%rbp)
	movq	-48(%rbp), %r11
	movq	%r11, -56(%rbp)
.L8:
	movq	$1, -64(%rbp)
	movq	-64(%rbp), %r11
	subq	-8(%rbp), %r11
	movq	%r11, -72(%rbp)
	cmpq	$0, -72(%rbp)
	jnz	.L9
.L41:
.L10:
	movq	-56(%rbp), %rdi
	callq	print_int
	movq	-56(%rbp), %rax
	jmp	.E_compute
.L9:
	movq	$2, -80(%rbp)
	pushq	%rdx
	movq	-8(%rbp), %rax
	cqto
	idivq	-80(%rbp)
	movq	%rdx, -88(%rbp)
	popq	%rdx
	movq	$0, -96(%rbp)
	movq	-96(%rbp), %r11
	subq	-88(%rbp), %r11
	movq	%r11, -104(%rbp)
	cmpq	$0, -104(%rbp)
	jz	.L13
.L42:
.L14:
	movq	$3, -112(%rbp)
	movq	-112(%rbp), %r11
	imulq	-8(%rbp), %r11
	movq	%r11, -120(%rbp)
	movq	$1, -128(%rbp)
	movq	-120(%rbp), %r11
	addq	-128(%rbp), %r11
	movq	%r11, -136(%rbp)
	movq	-136(%rbp), %r11
	movq	%r11, -8(%rbp)
.L15:
	movq	$1, -144(%rbp)
	movq	-56(%rbp), %r11
	addq	-144(%rbp), %r11
	movq	%r11, -152(%rbp)
	movq	-152(%rbp), %r11
	movq	%r11, -56(%rbp)
	jmp	.L8
.L13:
	movq	$2, -160(%rbp)
	pushq	%rdx
	movq	-8(%rbp), %rax
	cqto
	idivq	-160(%rbp)
	movq	%rax, -168(%rbp)
	popq	%rdx
	movq	-168(%rbp), %r11
	movq	%r11, -8(%rbp)
	jmp	.L15
.L0:
	movq	$0, -176(%rbp)
	movq	-176(%rbp), %rax
	jmp	.E_compute
.E_compute:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$88, %rsp
.L43:
	movq	$27, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$8, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$3, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	$0, -56(%rbp)
	movq	-56(%rbp), %r11
	movq	%r11, -64(%rbp)
	movq	-16(%rbp), %rdi
	movq	-32(%rbp), %rsi
	movq	-48(%rbp), %rdx
	callq	compute
	movq	%rax, -72(%rbp)
	movq	-72(%rbp), %r11
	movq	%r11, -64(%rbp)
	movq	-64(%rbp), %rdi
	callq	print_int
	movq	$0, -80(%rbp)
	movq	-80(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
