	.text
	.globl	compute
compute:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	%rdi, %rdi
	movq	%rsi, %rsi
	movq	%rdx, %rdx
	movq	%rcx, %rcx
.L52:
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
	movq	$0, %r8
.L16:
	movq	$1, %r8
.L17:
	movq	%rdi, %r11
	addq	%rsi, %r11
	movq	%r11, %r8
	addq	%rdx, %r8
	movq	%rdi, %r11
	subq	%rsi, %r11
	movq	%r11, %r8
	subq	%rdx, %r8
	movq	%rdi, %r11
	imulq	%rsi, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	imulq	%rdx, %r11
	movq	%r11, %r8
	pushq	%rdx
	movq	%rdi, %rax
	cqto
	idivq	%rsi
	movq	%rax, %r8
	popq	%rdx
	pushq	%rdx
	movq	%r8, %rax
	pushq	%r11
	movq	%rdx, %r11
	cqto
	idivq	%r11
	popq	%r11
	movq	%rax, %r8
	popq	%rdx
	pushq	%rdx
	movq	%rdi, %rax
	cqto
	idivq	%rsi
	movq	%rdx, %rsi
	popq	%rdx
	pushq	%rdx
	movq	%rsi, %rax
	pushq	%r11
	movq	%rdx, %r11
	cqto
	idivq	%r11
	popq	%r11
	movq	%rdx, %rsi
	popq	%rdx
	movq	%rsi, %rax
	movq	$2, %rax
	pushq	%rcx
	movq	%rdi, %r11
	movq	%rax, %rcx
	salq	%cl, %r11
	movq	%r11, %rsi
	popq	%rcx
	movq	%rsi, %rax
	movq	$2, %rsi
	pushq	%rcx
	movq	%rdi, %r11
	movq	%rsi, %rcx
	sarq	%cl, %r11
	movq	%r11, %rsi
	popq	%rcx
	movq	$0, %rsi
	movq	%rsi, %rdi
	cmpq	$0, %rcx
	jz	.L33
.L53:
.L34:
	movq	%rax, %rax
	jmp	.E_compute
.L33:
	movq	$1, %rdi
	jmp	.L34
.E_compute:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$120, %rsp
.L54:
	movq	$15, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$3, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$2, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	$0, -56(%rbp)
.L43:
	movq	$1, -56(%rbp)
.L44:
	movq	-56(%rbp), %r11
	movq	%r11, -64(%rbp)
	movq	$0, -72(%rbp)
	movq	-72(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	$0, -88(%rbp)
	cmpq	$0, -64(%rbp)
	jz	.L49
.L55:
.L48:
	movq	$1, -88(%rbp)
.L49:
	movq	-16(%rbp), %rdi
	movq	-32(%rbp), %rsi
	movq	-48(%rbp), %rdx
	movq	-88(%rbp), %rcx
	callq	compute
	movq	%rax, -96(%rbp)
	movq	-96(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	-80(%rbp), %rdi
	callq	print_int
	movq	$0, -104(%rbp)
	movq	-104(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
