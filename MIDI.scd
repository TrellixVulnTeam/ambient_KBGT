(
MIDIClient.init;

MIDIIn.connectAll;

MIDIFunc.trace(true);

SynthDef(\sin, {
	arg freq, harm=2, amp=0.01, out=0, gate=1;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = sig * 4;
	// sig = sig.softclip;
	sig = RHPF.ar(sig, (200 * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(
		Env.new([0, 0.05, 0.1, 0], [2, 3, 1], 'lin', releaseNode: 2),
		gate: gate,
		doneAction: 2
	);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

SynthDef(\sin_perc, {
	arg freq, harm=4, amp=0.1, out=0;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = RLPF.ar(sig, (freq * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(Env.perc(0.1, 2, 0.4), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

SynthDef(\saw, {
	arg freq=440, harm=4, amp=0.1, out=0, gate=1;
	var sig, env;
	sig = {Pulse.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = RLPF.ar(sig, (600 * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(
		Env.new([0, 0.8, 0.1, 0], [0.5, 3, 1.5], 'lin', releaseNode: 2),
		gate: gate,
		doneAction: 2
	);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

SynthDef(\saw_perc, {
	arg freq=440, harm=4, amp=1, out=0;
	var sig, env;
	sig = {LFSaw.ar(freq * Rand(-0.2, 0.2).midiratio)}!4;
	sig = Splay.ar(sig);
	sig = RLPF.ar(sig, (700 * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(Env.perc(0.1, 2, 0.8), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

MIDIdef.noteOn(\sin_1, {
	arg val, num, chan, src;
	~a = Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 1);

MIDIdef.noteOn(\sin_2, {
	arg val, num, chan, src;
	~b = Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 2);

MIDIdef.noteOn(\sin_3, {
	arg val, num, chan, src;
	~c = Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 3);

MIDIdef.noteOn(\sin_4, {
	arg val, num, chan, src;
	~d = Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 4);

MIDIdef.noteOn(\perc_1, {
	arg val, num, chan, src;
	Synth(\sin_perc, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 5);

MIDIdef.noteOn(\saw_1, {
	arg val, num, chan, src;
	~e = Synth(\saw, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 6);

MIDIdef.noteOn(\perc_2, {
	arg val, num, chan, src;
	Synth(\saw_perc, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 7);

MIDIdef.noteOff(\sin_off_1, {
	~a.set(\gate, 0)
}, chan: 1);

MIDIdef.noteOff(\sin_off_2, {
	~b.set(\gate, 0)
}, chan: 2);

MIDIdef.noteOff(\sin_off_3, {
	~c.set(\gate, 0)
}, chan: 3);

MIDIdef.noteOff(\sin_off_4, {
	~d.set(\gate, 0)
}, chan: 4);

MIDIdef.noteOff(\saw_off_1, {
	~e.set(\gate, 0);
}, chan: 6);
)
