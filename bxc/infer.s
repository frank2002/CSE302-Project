	.text
	.globl	foo
foo:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$232, %rsp
	movq	%rdi, %rcx
	movq	%rsi, %rdx
.L82:
	movq	$0, --1784(%rbp)
	movq	--1784(%rbp), %r11
	movq	%r11, --952(%rbp)
	movq	$0, --1400(%rbp)
	movq	--1400(%rbp), %r11
	movq	%r11, %r15
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, %r9
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, --248(%rbp)
	movq	$0, %rax
	movq	%rax, %r11
	movq	%r11, --1016(%rbp)
	movq	$0, --632(%rbp)
	movq	--632(%rbp), %r11
	movq	%r11, %rax
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --120(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1656(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %r13
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %rbx
	movq	$0, --568(%rbp)
	movq	--568(%rbp), %r11
	movq	%r11, --760(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --184(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1080(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1592(%rbp)
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1528(%rbp)
	movq	$0, --824(%rbp)
	movq	--824(%rbp), %r11
	movq	%r11, %rdx
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1720(%rbp)
	movq	$0, --696(%rbp)
	movq	--696(%rbp), %r11
	movq	%r11, --1336(%rbp)
	movq	$0, --312(%rbp)
	movq	--312(%rbp), %r11
	movq	%r11, %rsi
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %rdi
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, --1144(%rbp)
	movq	$0, --56(%rbp)
	movq	--56(%rbp), %r11
	movq	%r11, %r14
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %r12
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %r8
	movq	$0, %rcx
	movq	%rcx, %r11
	movq	%r11, %r10
	movq	$0, --1208(%rbp)
	movq	--1208(%rbp), %r11
	movq	%r11, %rcx
	movq	%r15, %r11
	addq	%r9, %r11
	movq	%r11, %r9
	movq	%r9, %r11
	addq	--248(%rbp), %r11
	movq	%r11, --1464(%rbp)
	movq	--1464(%rbp), %r11
	addq	--1016(%rbp), %r11
	movq	%r11, %r9
	movq	%r9, %r11
	addq	%rax, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--120(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1656(%rbp), %r11
	movq	%r11, --376(%rbp)
	movq	--376(%rbp), %r11
	addq	%r13, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rbx, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--760(%rbp), %r11
	movq	%r11, --440(%rbp)
	movq	--440(%rbp), %r11
	addq	--184(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1080(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1592(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1528(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rdx, %r11
	movq	%r11, --504(%rbp)
	movq	--504(%rbp), %r11
	addq	--1720(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1336(%rbp), %r11
	movq	%r11, --1272(%rbp)
	movq	--1272(%rbp), %r11
	addq	%rsi, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rdi, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	--1144(%rbp), %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%r14, %r11
	movq	%r11, --888(%rbp)
	movq	--888(%rbp), %r11
	addq	%r12, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%r8, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%r10, %r11
	movq	%r11, %rax
	movq	%rax, %r11
	addq	%rcx, %r11
	movq	%r11, %rax
	movq	%rax, %r11
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
