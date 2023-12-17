	.text
	.globl	foo
foo:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$312, %rsp
	movq	%rdi, %rcx
	movq	%rsi, %rdx
.L82:
	movq	$1, %rax
	movq	%rax, %r11
	movq	%r11, %rax
	movq	$1, -224(%rbp)
	movq	-224(%rbp), %r11
	movq	%r11, %r15
	movq	$1, -288(%rbp)
	movq	-288(%rbp), %r11
	movq	%r11, %r10
	movq	$1, %rax
	movq	%rax, %r11
	movq	%r11, -240(%rbp)
	movq	$1, -160(%rbp)
	movq	-160(%rbp), %r11
	movq	%r11, %rax
	movq	$1, %rcx
	movq	%rcx, %r11
	movq	%r11, %r8
	movq	$1, %rcx
	movq	%rcx, %r11
	movq	%r11, -200(%rbp)
	movq	$1, %rcx
	movq	%rcx, %r11
	movq	%r11, %r9
	movq	$1, -56(%rbp)
	movq	-56(%rbp), %r11
	movq	%r11, -232(%rbp)
	movq	$0, -168(%rbp)
	movq	-168(%rbp), %r11
	movq	%r11, %rdi
	movq	$0, -32(%rbp)
	movq	-32(%rbp), %r11
	movq	%r11, -296(%rbp)
	movq	$0, -88(%rbp)
	movq	-88(%rbp), %r11
	movq	%r11, -192(%rbp)
	movq	$0, -144(%rbp)
	movq	-144(%rbp), %r11
	movq	%r11, -152(%rbp)
	movq	$0, -64(%rbp)
	movq	-64(%rbp), %r11
	movq	%r11, %r12
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, -176(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, -208(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %rbx
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %rsi
	movq	$0, -304(%rbp)
	movq	-304(%rbp), %r11
	movq	%r11, -40(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, -216(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %rdx
	movq	$0, -272(%rbp)
	movq	-272(%rbp), %r11
	movq	%r11, -264(%rbp)
	movq	$0, -136(%rbp)
	movq	-136(%rbp), %r11
	movq	%r11, %rcx
	movq	$0, -16(%rbp)
	movq	-16(%rbp), %r11
	movq	%r11, %r14
	movq	$0, -184(%rbp)
	movq	-184(%rbp), %r11
	movq	%r11, -248(%rbp)
	movq	$0, -120(%rbp)
	movq	-120(%rbp), %r11
	movq	%r11, %r13
	movq	%r15, %r11
	addq	%r10, %r11
	movq	%r11, %r10
	movq	%r10, %r11
	addq	-240(%rbp), %r11
	movq	%r11, -80(%rbp)
	movq	-80(%rbp), %r11
	addq	%rax, %r11
	movq	%r11, -72(%rbp)
	movq	-72(%rbp), %r11
	addq	%r8, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-200(%rbp), %r11
	movq	%r11, -48(%rbp)
	movq	-48(%rbp), %r11
	addq	%r9, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-232(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rdi, %r11
	movq	%r11, -112(%rbp)
	movq	-112(%rbp), %r11
	addq	-296(%rbp), %r11
	movq	%r11, -256(%rbp)
	movq	-256(%rbp), %r11
	addq	-192(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-152(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%r12, %r11
	movq	%r11, -128(%rbp)
	movq	-128(%rbp), %r11
	addq	-176(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-208(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rbx, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rsi, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-40(%rbp), %r11
	movq	%r11, -96(%rbp)
	movq	-96(%rbp), %r11
	addq	-216(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rdx, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	-264(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rcx, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%r14, %r11
	movq	%r11, -104(%rbp)
	movq	-104(%rbp), %r11
	addq	-248(%rbp), %r11
	movq	%r11, -280(%rbp)
	movq	-280(%rbp), %r11
	addq	%r13, %r11
	movq	%r11, -24(%rbp)
	movq	-24(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %rax
	jmp	.E_foo
.E_foo:
	movq	%rbp, %rsp
	popq	%rbp
	retq
	.text
	.globl	main
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$56, %rsp
.L83:
	movq	$0, -8(%rbp)
	movq	-8(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	$1, -24(%rbp)
	movq	$2, -32(%rbp)
	movq	-24(%rbp), %rdi
	movq	-32(%rbp), %rsi
	callq	foo
	movq	%rax, -40(%rbp)
	movq	-40(%rbp), %r11
	movq	%r11, -16(%rbp)
	movq	-16(%rbp), %rdi
	callq	print_int
	movq	$0, -48(%rbp)
	movq	-48(%rbp), %rax
	jmp	.E_main
.E_main:
	movq	%rbp, %rsp
	popq	%rbp
	retq
