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
.L60:
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	$0, %r8
.L16:
	movq	$1, %r8
.L17:
	movq	%r8, %r11
	movq	%r11, %r8
	movq	%rdi, %r11
	addq	%rsi, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	addq	%rdx, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	%rdi, %r11
	subq	%rsi, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	subq	%rdx, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	movq	%r11, %r8
	movq	%rdi, %r11
	imulq	%rsi, %r11
	movq	%r11, %r8
	movq	%r8, %r11
	imulq	%rdx, %r11
	movq	%r11, %r8
	movq	%r8, %r11
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
	movq	%r8, %r11
	movq	%r11, %r8
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
	movq	%rsi, %r11
	movq	%r11, %rax
	movq	$2, %rax
	pushq	%rcx
	movq	%rdi, %r11
	movq	%rax, %rcx
	salq	%cl, %r11
	movq	%r11, %rax
	popq	%rcx
	movq	%rax, %r11
	movq	%r11, %rax
	movq	$2, %rax
	pushq	%rcx
	movq	%rdi, %r11
	movq	%rax, %rcx
	sarq	%cl, %r11
	movq	%r11, %rax
	popq	%rcx
	movq	%rax, %r11
	movq	%r11, %rax
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, %rdi
	cmpq	$0, %rcx
	jz	.L33
.L61:
.L34:
	movq	%rdi, %r11
	movq	%r11, %rax
	movq	%rax, %rax
	jmp	.E_compute
.L33:
	movq	$1, %rdi
	movq	%rdi, %r11
	movq	%r11, %rdi
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
	subq	$136, %rsp
.L62:
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
.L47:
	movq	$1, -72(%rbp)
.L48:
	movq	-72(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	$0, -88(%rbp)
	movq	$0, -96(%rbp)
	cmpq	$0, -64(%rbp)
	jz	.L54
.L63:
.L53:
	movq	$1, -96(%rbp)
.L54:
	movq	-16(%rbp), %rdi
	movq	-32(%rbp), %rsi
	movq	-48(%rbp), %rdx
	movq	-96(%rbp), %rcx
	callq	compute
	movq	%rax, -104(%rbp)
	cmpq	$0, -104(%rbp)
	jz	.L51
.L64:
.L50:
	movq	$1, -88(%rbp)
.L51:
	movq	-88(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	$0, -112(%rbp)
	cmpq	$0, -80(%rbp)
	jz	.L58
.L65:
.L57:
	movq	$1, -112(%rbp)
.L58:
	movq	-112(%rbp), %rdi
	callq	print_bool
	movq	$0, -120(%rbp)
	movq	-120(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
