	.text
	.globl	compute
compute:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$488, %rsp
	movq	%rdi, %rdi
	movq	%rsi, %rsi
	movq	%rdx, %rdx
	movq	%rcx, %rcx
.L90:
	movq	$0, -376(%rbp)
	movq	%rsi, %r11
	subq	%rdi, %r11
	movq	%r11, -64(%rbp)
	movq	-376(%rbp), %r11
	movq	%r11, -416(%rbp)
	movq	%rdx, %r8
	movq	%rdi, -104(%rbp)
	movq	%rcx, -48(%rbp)
	cmpq	$0, -64(%rbp)
	jl	.L2
.L91:
.L3:
	movq	-416(%rbp), %r11
	movq	%r11, -296(%rbp)
	movq	$0, -184(%rbp)
	movq	-184(%rbp), %r11
	movq	%r11, -248(%rbp)
	movq	-184(%rbp), %r11
	movq	%r11, -248(%rbp)
	cmpq	$0, -296(%rbp)
	jz	.L7
.L92:
.L8:
	movq	%rcx, %r11
	subq	%rdx, %r11
	movq	%r11, -80(%rbp)
	cmpq	$0, -80(%rbp)
	jl	.L7
.L93:
.L6:
	movq	$1, %r8
	movq	%r8, -248(%rbp)
.L7:
	movq	-248(%rbp), %r10
	movq	$0, -176(%rbp)
	movq	-176(%rbp), %r11
	movq	%r11, -360(%rbp)
	movq	-360(%rbp), %r11
	movq	%r11, -200(%rbp)
	movq	%r10, -128(%rbp)
.L12:
	movq	%rsi, %r11
	subq	-104(%rbp), %r11
	movq	%r11, %r12
	movq	%r8, -72(%rbp)
	movq	-48(%rbp), %r13
	cmpq	$0, %r12
	jg	.L13
.L94:
.L14:
	movq	$0, -152(%rbp)
	movq	-152(%rbp), %r11
	movq	%r11, -392(%rbp)
	movq	-152(%rbp), %r11
	movq	%r11, -392(%rbp)
	cmpq	$0, -128(%rbp)
	jz	.L65
.L102:
.L66:
	movq	$100, -424(%rbp)
	movq	-424(%rbp), %r11
	subq	-200(%rbp), %r11
	movq	%r11, -16(%rbp)
	cmpq	$0, -16(%rbp)
	jl	.L64
.L103:
.L65:
	movq	-392(%rbp), %rdi
	movq	$0, -432(%rbp)
	movq	-432(%rbp), %rcx
	cmpq	$0, %rdi
	jz	.L72
.L104:
.L71:
	movq	-200(%rbp), %r11
	imulq	-104(%rbp), %r11
	movq	%r11, -304(%rbp)
	movq	-304(%rbp), %r11
	addq	%rsi, %r11
	movq	%r11, -464(%rbp)
	movq	-464(%rbp), %r11
	subq	%r8, %r11
	movq	%r11, -120(%rbp)
	movq	-120(%rbp), %r11
	movq	%r11, -352(%rbp)
	movq	-352(%rbp), %rax
.L73:
	movq	%rax, %rax
	jmp	.E_compute
.L72:
	pushq	%rax
	pushq	%rdx
	movq	-200(%rbp), %rax
	cqto
	idivq	-48(%rbp)
	movq	%rdx, -160(%rbp)
	popq	%rdx
	popq	%rax
	movq	-160(%rbp), %r11
	movq	%r11, -208(%rbp)
	movq	-208(%rbp), %rax
	jmp	.L73
.L64:
	movq	$1, -264(%rbp)
	movq	-264(%rbp), %r11
	movq	%r11, -392(%rbp)
	jmp	.L65
.L13:
	movq	-200(%rbp), %r11
	addq	-104(%rbp), %r11
	movq	%r11, -328(%rbp)
	movq	-328(%rbp), %r11
	addq	%r8, %r11
	movq	%r11, %r12
	movq	%r12, %r11
	subq	-48(%rbp), %r11
	movq	%r11, -320(%rbp)
	movq	-320(%rbp), %r11
	movq	%r11, -400(%rbp)
	movq	$1, -456(%rbp)
	movq	-104(%rbp), %r11
	addq	-456(%rbp), %r11
	movq	%r11, -448(%rbp)
	movq	-448(%rbp), %r12
	movq	$2, -224(%rbp)
	pushq	%rax
	pushq	%rdx
	movq	%r12, %rax
	cqto
	idivq	-224(%rbp)
	movq	%rdx, -368(%rbp)
	popq	%rdx
	popq	%rax
	movq	$0, -336(%rbp)
	movq	-336(%rbp), %r11
	subq	-368(%rbp), %r11
	movq	%r11, -96(%rbp)
	movq	%r12, -104(%rbp)
	cmpq	$0, -96(%rbp)
	jz	.L21
.L95:
.L22:
	pushq	%rax
	pushq	%rdx
	movq	%rsi, %rax
	cqto
	idivq	%r12
	movq	%rdx, -40(%rbp)
	popq	%rdx
	popq	%rax
	movq	-48(%rbp), %r11
	addq	-40(%rbp), %r11
	movq	%r11, %r13
	movq	$1, %r14
	pushq	%rcx
	movq	%r13, %r11
	movq	%r14, %rcx
	sarq	%cl, %r11
	movq	%r11, -216(%rbp)
	popq	%rcx
	movq	-216(%rbp), %r11
	movq	%r11, -88(%rbp)
	movq	-88(%rbp), %r13
.L23:
	movq	$0, -232(%rbp)
	movq	-72(%rbp), %r8
	movq	%r13, -48(%rbp)
	movq	-232(%rbp), %r11
	movq	%r11, -136(%rbp)
	cmpq	$0, -128(%rbp)
	jz	.L39
.L96:
.L37:
	movq	$1, -240(%rbp)
	movq	-240(%rbp), %r11
	movq	%r11, -136(%rbp)
.L38:
	movq	-136(%rbp), %r14
	movq	%r14, -128(%rbp)
	cmpq	$0, %r14
	jz	.L42
.L98:
.L44:
	movq	$50, %r8
	movq	%r8, %r11
	subq	-400(%rbp), %r11
	movq	%r11, -112(%rbp)
	cmpq	$0, -112(%rbp)
	jl	.L41
.L99:
.L42:
	cmpq	$0, %r14
	jz	.L53
.L100:
.L51:
	movq	$2, -312(%rbp)
	movq	-400(%rbp), %r11
	imulq	-312(%rbp), %r11
	movq	%r11, -344(%rbp)
	movq	-344(%rbp), %r11
	movq	%r11, -472(%rbp)
	movq	-472(%rbp), %r11
	movq	%r11, -256(%rbp)
.L52:
	movq	-256(%rbp), %r11
	movq	%r11, -408(%rbp)
.L43:
	movq	-408(%rbp), %r11
	movq	%r11, -200(%rbp)
	jmp	.L12
.L53:
	movq	$50, %r8
	movq	%r8, %r11
	subq	-400(%rbp), %r11
	movq	%r11, -32(%rbp)
	cmpq	$0, -32(%rbp)
	jge	.L50
.L101:
	jmp	.L51
.L50:
	movq	%r12, %r11
	addq	%rsi, %r11
	movq	%r11, -24(%rbp)
	movq	$10, -56(%rbp)
	pushq	%rax
	pushq	%rdx
	movq	-24(%rbp), %rax
	cqto
	idivq	-56(%rbp)
	movq	%rax, -272(%rbp)
	popq	%rdx
	popq	%rax
	movq	-400(%rbp), %r11
	addq	-272(%rbp), %r11
	movq	%r11, %r8
	movq	%r8, %r9
	movq	%r9, -256(%rbp)
	jmp	.L52
.L41:
	movq	%r12, %r11
	imulq	%r13, %r11
	movq	%r11, -192(%rbp)
	pushq	%rax
	pushq	%rdx
	movq	-192(%rbp), %rax
	cqto
	idivq	-72(%rbp)
	movq	%rdx, -480(%rbp)
	popq	%rdx
	popq	%rax
	movq	-400(%rbp), %r11
	subq	-480(%rbp), %r11
	movq	%r11, %r8
	movq	%r8, %rbx
	movq	%rbx, -408(%rbp)
	jmp	.L43
.L39:
	movq	%r13, %r11
	subq	-400(%rbp), %r11
	movq	%r11, %r8
	cmpq	$0, %r8
	jg	.L37
.L97:
	jmp	.L38
.L21:
	pushq	%rax
	pushq	%rdx
	movq	%rsi, %rax
	cqto
	idivq	%r12
	movq	%rdx, -288(%rbp)
	popq	%rdx
	popq	%rax
	movq	%r8, %r11
	addq	-288(%rbp), %r11
	movq	%r11, -384(%rbp)
	movq	$1, -144(%rbp)
	pushq	%rcx
	movq	-384(%rbp), %r11
	movq	-144(%rbp), %rcx
	salq	%cl, %r11
	movq	%r11, -280(%rbp)
	popq	%rcx
	movq	-280(%rbp), %r11
	movq	%r11, -440(%rbp)
	movq	-440(%rbp), %r11
	movq	%r11, -72(%rbp)
	jmp	.L23
.L2:
	movq	$1, -168(%rbp)
	movq	-168(%rbp), %r11
	movq	%r11, -416(%rbp)
	jmp	.L3
.E_compute:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$104, %rsp
.L105:
	movq	$5, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$25, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, -32(%rbp)
	movq	$15, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	$10, -56(%rbp)
	movq	-56(%rbp), %r11
	movq	%r11, -64(%rbp)
	movq	$0, -72(%rbp)
	movq	-72(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	-16(%rbp), %rdi
	movq	-32(%rbp), %rsi
	movq	-48(%rbp), %rdx
	movq	-64(%rbp), %rcx
	callq	compute
	movq	%rax, -88(%rbp)
	movq	-88(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	-80(%rbp), %rdi
	callq	print_int
	movq	$0, -96(%rbp)
	movq	-96(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
