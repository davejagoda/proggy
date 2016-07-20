#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

lower =   0; /* lower limit of temperature table */
upper = 300; /* upper limit of temperature table */
step  =  20; /* step size */

fahr = lower;
while (fahr <= upper) {
    celsius = (5.0/9.0) * (fahr-32.0);
    print(fahr, celsius.toFixed(1));
    fahr = fahr + step;
}
