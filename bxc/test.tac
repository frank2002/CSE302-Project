[proc @compute('%a', '%b', '%c', '%d'):
    .L90:;
    %1.160 = const 0;
    %4.161 = sub '%b', '%a';
    %1.35 = copy '%1.160';
    %c.67 = copy '%c';
    %a.70 = copy '%a';
    %d.71 = copy '%d';
    jlt '%4.161', '.L2';
    .L91:;
    .L3:;
    %0.38 = copy '%1.35';
    %5.39 = const 0;
    %5.78 = copy '%5.39';
    %5.78 = copy '%5.39';
    jz '%0.38', '.L7';
    .L92:;
    .L8:;
    %9.12 = sub '%d', '%c';
    jlt '%9.12', '.L7';
    .L93:;
    .L6:;
    %5.66 = const 1;
    %5.78 = copy '%5.66';
    .L7:;
    %0.79 = copy '%5.78';
    %11.80 = const 0;
    %10.81 = copy '%11.80';
    %10.68 = copy '%10.81';
    %0.72 = copy '%0.79';
    .L12:;
    %15.73 = sub '%b', '%a.70';
    %c.171 = copy '%c.67';
    %d.175 = copy '%d.71';
    jgt '%15.73', '.L13';
    .L94:;
    .L14:;
    %63.262 = const 0;
    %63.166 = copy '%63.262';
    %63.166 = copy '%63.262';
    jz '%0.72', '.L65';
    .L102:;
    .L66:;
    %67.154 = const 100;
    %68.155 = sub '%67.154', '%10.68';
    jlt '%68.155', '.L64';
    .L103:;
    .L65:;
    %62.168 = copy '%63.166';
    %70.169 = const 0;
    %69.170 = copy '%70.169';
    jz '%62.168', '.L72';
    .L104:;
    .L71:;
    %76.53 = mul '%10.68', '%a.70';
    %75.54 = add '%76.53', '%b';
    %74.55 = sub '%75.54', '%c.67';
    %69.56 = copy '%74.55';
    %69.242 = copy '%69.56';
    .L73:;
    ret '%69.242';
    .L72:;
    %77.15 = mod '%10.68', '%d.71';
    %69.16 = copy '%77.15';
    %69.242 = copy '%69.16';
    jmp '.L73';
    .L64:;
    %63.255 = const 1;
    %63.166 = copy '%63.255';
    jmp '.L65';
    .L13:;
    %18.126 = add '%10.68', '%a.70';
    %17.127 = add '%18.126', '%c.67';
    %16.128 = sub '%17.127', '%d.71';
    %10.129 = copy '%16.128';
    %20.130 = const 1;
    %19.131 = add '%a.70', '%20.130';
    %a.132 = copy '%19.131';
    %25.133 = const 2;
    %24.134 = mod '%a.132', '%25.133';
    %26.135 = const 0;
    %27.136 = sub '%26.135', '%24.134';
    %a.70 = copy '%a.132';
    jz '%27.136', '.L21';
    .L95:;
    .L22:;
    %34.231 = mod '%b', '%a.132';
    %33.232 = add '%d.71', '%34.231';
    %35.233 = const 1;
    %32.234 = shr '%33.232', '%35.233';
    %d.235 = copy '%32.234';
    %d.175 = copy '%d.235';
    .L23:;
    %36.177 = const 0;
    %c.67 = copy '%c.171';
    %d.71 = copy '%d.175';
    %36.86 = copy '%36.177';
    jz '%0.72', '.L39';
    .L96:;
    .L37:;
    %36.110 = const 1;
    %36.86 = copy '%36.110';
    .L38:;
    %0.88 = copy '%36.86';
    %0.72 = copy '%0.88';
    jz '%0.88', '.L42';
    .L98:;
    .L44:;
    %45.293 = const 50;
    %46.294 = sub '%45.293', '%10.129';
    jlt '%46.294', '.L41';
    .L99:;
    .L42:;
    jz '%0.88', '.L53';
    .L100:;
    .L51:;
    %61.46 = const 2;
    %60.47 = mul '%10.129', '%61.46';
    %10.48 = copy '%60.47';
    %10.264 = copy '%10.48';
    .L52:;
    %10.270 = copy '%10.264';
    .L43:;
    %10.68 = copy '%10.270';
    jmp '.L12';
    .L53:;
    %54.217 = const 50;
    %55.218 = sub '%54.217', '%10.129';
    jge '%55.218', '.L50';
    .L101:;
    jmp '.L51';
    .L50:;
    %58.23 = add '%a.132', '%b';
    %59.24 = const 10;
    %57.25 = div '%58.23', '%59.24';
    %56.26 = add '%10.129', '%57.25';
    %10.27 = copy '%56.26';
    %10.264 = copy '%10.27';
    jmp '.L52';
    .L41:;
    %49.196 = mul '%a.132', '%d.175';
    %48.197 = mod '%49.196', '%c.171';
    %47.198 = sub '%10.129', '%48.197';
    %10.199 = copy '%47.198';
    %10.270 = copy '%10.199';
    jmp '.L43';
    .L39:;
    %40.249 = sub '%d.175', '%10.129';
    jgt '%40.249', '.L37';
    .L97:;
    jmp '.L38';
    .L21:;
    %30.206 = mod '%b', '%a.132';
    %29.207 = add '%c.67', '%30.206';
    %31.208 = const 1;
    %28.209 = shl '%29.207', '%31.208';
    %c.210 = copy '%28.209';
    %c.171 = copy '%c.210';
    jmp '.L23';
    .L2:;
    %1.32 = const 1;
    %1.35 = copy '%1.32';
    jmp '.L3';
]