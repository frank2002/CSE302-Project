[proc @compute('%x', '%y', '%z'):
    .L38:;
    %3.39 = const 0;
    %4.40 = sub '%3.39', '%x';
    %x.35 = copy '%x';
    jge '%4.40', '.L0';
    .L39:;
    .L1:;
    .L2:;
    %7.9 = const 0;
    %6.10 = copy '%7.9';
    %6.34 = copy '%6.10';
    .L8:;
    %11.36 = const 1;
    %12.37 = sub '%11.36', '%x.35';
    jnz '%12.37', '.L9';
    .L41:;
    .L10:;
    ret '%6.34';
    .L9:;
    %17.13 = const 2;
    %16.14 = mod '%x.35', '%17.13';
    %18.15 = const 0;
    %19.16 = sub '%18.15', '%16.14';
    jz '%19.16', '.L13';
    .L42:;
    .L14:;
    %24.19 = const 3;
    %23.20 = mul '%24.19', '%x.35';
    %25.21 = const 1;
    %22.22 = add '%23.20', '%25.21';
    %x.23 = copy '%22.22';
    %x.4 = copy '%x.23';
    .L15:;
    %27.5 = const 1;
    %26.6 = add '%6.34', '%27.5';
    %6.7 = copy '%26.6';
    %6.34 = copy '%6.7';
    %x.35 = copy '%x.4';
    jmp '.L8';
    .L13:;
    %21.27 = const 2;
    %20.28 = div '%x.35', '%21.27';
    %x.29 = copy '%20.28';
    %x.4 = copy '%x.29';
    jmp '.L15';
    .L0:;
    %5.30 = const 0;
    ret '%5.30';
]