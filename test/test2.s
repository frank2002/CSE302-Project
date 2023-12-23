	.text
	.globl	compute
compute:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	%rdi, %rdi
	movq	%rsi, %rsi
	movq	%rdx, %rdx
.L38:
	movq	$0, %rcx
	subq	%rdi, %rcx
	movq	%rdi, %rbx
	cmpq	$0, %rcx
	jge	.L0
.L39:
.L1:
.L2:
	movq	$0, %rbx
	movq	%rbx, %rcx
	movq	%rcx, %rax
.L8:
	movq	$1, %rsi
	subq	%rbx, %rsi
	cmpq	$0, %rsi
	jnz	.L9
.L41:
.L10:
	movq	%rax, %rax
	jmp	.E_compute
.L9:
	movq	$2, %rsi
	pushq	%rax
	pushq	%rdx
	movq	%rbx, %rax
	cqto
	idivq	%rsi
	movq	%rdx, %rsi
	popq	%rdx
	popq	%rax
	movq	$0, %r10
	movq	%r10, %r11
	subq	%rsi, %r11
	movq	%r11, %rsi
	cmpq	$0, %rsi
	jz	.L13
.L42:
.L14:
	movq	$3, %rsi
	movq	%rsi, %r11
	imulq	%rbx, %r11
	movq	%r11, %r8
	movq	$1, %rsi
	movq	%r8, %r11
	addq	%rsi, %r11
	movq	%r11, %rsi
	movq	%rsi, %r8
	movq	%r8, %rsi
.L15:
	movq	$1, %r10
	movq	%rax, %r11
	addq	%r10, %r11
	movq	%r11, %rbx
	movq	%rbx, %r10
	movq	%rsi, %rbx
	movq	%r10, %rax
	jmp	.L8
.L13:
	movq	$2, %rsi
	pushq	%rax
	pushq	%rdx
	movq	%rbx, %rax
	cqto
	idivq	%rsi
	movq	%rax, %rsi
	popq	%rdx
	popq	%rax
	movq	%rsi, %r9
	movq	%r9, %rsi
	jmp	.L15
.L0:
	movq	$0, %rax
	movq	%rax, %rax
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
