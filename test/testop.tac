[proc @compute('%x', '%y', '%z', '%b'):
    .L52:;
    %1.12 = const 0;
    %0.13 = copy '%1.12';
    %3.14 = const 0;
    %2.15 = copy '%3.14';
    %5.16 = const 0;
    %4.17 = copy '%5.16';
    %7.18 = const 0;
    %6.19 = copy '%7.18';
    %9.20 = const 0;
    %8.21 = copy '%9.20';
    %11.22 = const 0;
    %10.23 = copy '%11.22';
    %13.24 = const 0;
    %12.25 = copy '%13.24';
    %15.26 = const 0;
    .L16:;
    %15.59 = const 1;
    .L17:;
    %14.32 = copy '%15.59';
    %19.33 = add '%x', '%y';
    %18.34 = add '%19.33', '%z';
    %0.35 = copy '%18.34';
    %21.36 = sub '%x', '%y';
    %20.37 = sub '%21.36', '%z';
    %2.38 = copy '%20.37';
    %23.39 = mul '%x', '%y';
    %22.40 = mul '%23.39', '%z';
    %4.41 = copy '%22.40';
    %25.42 = div '%x', '%y';
    %24.43 = div '%25.42', '%z';
    %6.44 = copy '%24.43';
    %27.45 = mod '%x', '%y';
    %26.46 = mod '%27.45', '%z';
    %8.47 = copy '%26.46';
    %29.48 = const 2;
    %28.49 = shl '%x', '%29.48';
    %10.50 = copy '%28.49';
    %31.51 = const 2;
    %30.52 = shr '%x', '%31.51';
    %12.53 = copy '%30.52';
    %32.54 = const 0;
    %32.1 = copy '%32.54';
    jz '%b', '.L33';
    .L53:;
    .L34:;
    %14.3 = copy '%32.1';
    ret '%10.50';
    .L33:;
    %32.5 = const 1;
    %32.1 = copy '%32.5';
    jmp '.L34';
]