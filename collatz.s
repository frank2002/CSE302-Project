	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$128, %rsp
.L24:
	movq	$837799, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
.L2:
.L3:
	movq	-16(%rbp), %rdi
	callq	print_int
	movq	$1, -24(%rbp)
	movq	-24(%rbp), %r11
	subq	-16(%rbp), %r11
	movq	%r11, -32(%rbp)
	cmpq	$0, -32(%rbp)
	jz	.L5
.L25:
.L6:
.L7:
	movq	$2, -40(%rbp)
	movq	-16(%rbp), %rax
	cqto
	idivq	-40(%rbp)
	movq	%rdx, -48(%rbp)
	movq	$0, -56(%rbp)
	movq	-56(%rbp), %r11
	subq	-48(%rbp), %r11
	movq	%r11, -64(%rbp)
	cmpq	$0, -64(%rbp)
	jz	.L10
.L27:
.L11:
	movq	$3, -72(%rbp)
	movq	-72(%rbp), %rax
	imulq	-16(%rbp)
	movq	%rax, -80(%rbp)
	movq	$1, -88(%rbp)
	movq	-80(%rbp), %r11
	addq	-88(%rbp), %r11
	movq	%r11, -96(%rbp)
	movq	-96(%rbp), %r11
	movq	%r11, -16(%rbp)
.L12:
	jmp	.L2
.L10:
	movq	$2, -104(%rbp)
	movq	-16(%rbp), %rax
	cqto
	idivq	-104(%rbp)
	movq	%rax, -112(%rbp)
	movq	-112(%rbp), %r11
	movq	%r11, -16(%rbp)
	jmp	.L12
.L5:
.L4:
	movq	$0, -120(%rbp)
	movq	-120(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
