# Style library — Caseread.ai LinkedIn voice

This is the running style library. The seed content below was extracted from Collin's full LinkedIn posting history (23 posts over ~2 months) and serves as the primary tone anchor for the linkedin-post-generator skill.

The library grows over time. As Collin curates LinkedIn posts he likes from his feed, he forwards them to the bot as Telegram screenshots and the screenshot-ingester skill (planned) appends new dated entries. Each entry captures a structural move worth carrying forward, not the original poster's identity.

---

## Seed: Collin's LinkedIn voice — 23 posts, ~2 months of history

### Key facts to lock in

- **Brand**: Caseread.ai (rebranded from Lawless.ai 2026-05-08, publicly announced on LinkedIn). Bio reads "Founder @ Caseread.ai | Legal Technology". 910 followers.
- **Cofounder/COO**: Rey Alonzo, JD, MBA (named in posts; he engages publicly).
- **Audience**: solo + small + mid-market law firms (1-100 attorneys). "Mid-market" appears repeatedly. Not just solos.
- **Identity Collin uses**: "I'm a CS student" — leans into outsider/builder angle when it serves him.
- **Major partnership**: OpenLaws (~Apr 2026) — 4.5M statutes, 10.3M opinions, all 50 states + federal.
- **Free public tool**: Hallucination Shield at trylawless.com/verify — citation checker, no signup.
- **Recurring foils**: Westlaw ($200-400/seat/mo), Lexis+ AI (17% hallucination), CoCounsel/Harvey ($11B valuation), Big Two data monopoly.

### Voice patterns observed (from real posts)

#### Opening hooks (his signature)

- "Are your clients using ChatGPT or Claude on their own cases?" (question opener)
- "Westlaw hasn't meaningfully innovated in 20 years." (declarative provocation)
- "AI is only as capable as the framework around it." (architectural assertion)
- "Stanford found that Westlaw's AI hallucinates 33% of the time. Lexis+ AI? 17%." (stat opener)
- "The law is public. It always has been." (3-word punch)
- "'Why aren't you charging yet?'" (quoted question opener)
- "Every attorney I talk to asks the same question:" (lead with consensus)
- "480+ lawyers have been caught submitting AI-hallucinated citations to courts." (alarming stat)
- "Lawless.ai is now Caseread.ai" (declarative announcement)

#### Body structure

- Short paragraphs (1-3 sentences)
- Line breaks between thoughts
- Often uses bullet arrows (→) for enumerated items, not standard bullets
- Concrete numbers: $400/seat/month, $15k/year, 480 lawyers, 33%, 17%
- Names specific products as foils: Westlaw, Lexis+ AI, ChatGPT, CoCounsel, Harvey
- Cites real cases by name + judge: Heppner / Rakoff
- Cites real doctrines: Kovel, ABA Rule 1.6, FRCP, attorney-client privilege

#### Tone moves

- Self-aware ("Cute in a pitch deck. Less cute on a firm's engagement letter.")
- Confident-not-arrogant ("Caseread.ai isn't trying to be a cheaper Westlaw. We're trying to make Westlaw irrelevant.")
- Builder voice ("I'm building", "We're in beta", "I built")
- Mission-tinged closers ("The law belongs to everyone. Act accordingly.")
- Doesn't apologize for being a student

#### Endings (what he DOES)

- Implications, not CTAs ("That's the door legal tech needs to walk through.")
- Concrete next-action invites ("Go to trylawless.com and become a beta tester.")
- Quiet conviction ("Onward.")
- Specific URL or product reference (trylawless.com, Caseread.ai)
- Tag company page (Caseread.ai)

#### Endings (what he DOESN'T)

- "What do you think?"
- "Drop your thoughts below"
- "Like and share"
- Hedging close ("Just my two cents")

#### Hashtag use

- 0-5 trailing hashtags, often a mix
- Common ones: `#legaltech`, `#AI`, `#legalresearch`, `#lawfirm`, `#startup`, `#LegalAI`, `#AIsafety`, `#BuildInPublic`, `#ABA1_6`
- Some posts use 0 hashtags

#### Engagement note

- Highest-impression posts: Heppner case analysis (5,032), framework/architecture (4,222 + 2,460 edited), Westlaw monopoly (4,479).
- Lowest-impression posts: simple beta-tester recruiting (135-236).
- Pattern: substantive, opinionated, legally-grounded posts dramatically outperform simple "try our beta" posts.

---

## Seed: top-performing post archetypes (use as Pillar templates)

### Pillar A template — Heppner case analysis (5,032 impressions)

> Are your clients using ChatGPT or Claude on their own cases?
>
> If they are, those conversations probably aren't privileged. A federal judge ruled on it this year.
>
> In United States v. Heppner, Judge Rakoff held that documents a defendant created with a public AI tool, independently and without his lawyer's direction, were not protected by attorney-client privilege or the work product doctrine. Three reasons: the platform is a third party with no confidentiality obligation, the client wasn't acting at counsel's direction, and the tool's privacy policy explicitly permitted data collection and disclosure.
>
> The case isn't about attorneys waiving privilege through their own AI use. It's about clients independently using consumer AI, and the resulting documents being unprotected.
>
> What this means for attorneys:
> Clients will use AI on their own cases. They already are. "Asking ChatGPT" feels private to them. Legally, it's a third-party disclosure. Address it in the engagement letter.
>
> For internal AI use, the bar is enterprise-grade confidentiality, no training on your data, isolated tenancy, and counsel-directed use. The Heppner court signaled that AI used as a counsel-directed agent could potentially fall within the Kovel doctrine. That's the door legal tech needs to walk through.
>
> This is exactly why Caseread.ai was built. Every firm gets a completely isolated database. Documents never touch another firm's data. Inputs are never used to train models. Your data stays in your vault.

**Template lessons**: Open with provocative question. Cite specific case + judge. Three-reasons structure. Translate doctrine into practical attorney advice. End with subtle product tie-in.

### Pillar A template — Framework/architecture (4,222 impressions)

> AI is only as capable as the framework around it.
>
> Most "AI products" in legal tech are GPT wrappers. A text box, an API call, and a prayer that the output is correct.
>
> That's not a product. That's a liability.
>
> The AI model is maybe 20% of the problem. The other 80% is everything around it:
> → Where does the data come from? Is it real case law or a hallucination?
> → Are citations verified before they reach the lawyer?
> → Is client data isolated or mixed with everyone else's?
> → What happens when the model is wrong?
>
> Strip away the framework and the smartest AI in the world is still just confidently guessing.
>
> That changes what legal tech creators have to build. When dealing with AI, results have to be perfect. 95% isn't good enough when it comes to people's careers.
>
> That's why we built Caseread.ai the way we did, every citation verified, every firm's data isolated, every answer traceable to its source with a link. Not because it's easier. Because lawyers deserve tools they can actually trust.

**Template lessons**: Open with one-line architectural assertion. Use "→" arrow bullets for enumerated technical-meets-business questions. Pivot to ethics-of-tolerance ("95% isn't good enough"). Close with values, not features.

### Pillar B template — "Why aren't you charging yet?" (928 impressions, very on-voice)

> "Why aren't you charging yet?"
>
> Investors ask. Mentors ask. Other founders ask.
>
> The standard for software says charge early. Validate with revenue. Ship fast, fix later.
>
> For most products, that works. For legal tech, it doesn't.
>
> A bad recommendation in e-commerce costs a return. A bad citation in a legal brief costs a career. We're not going to be the tool that contributes to that.
>
> But it's not just about AI accuracy. Lawyers don't just need smart answers, they need a platform that fits how they actually work:
> → Bulk uploading hundreds of case documents without friction
> → Organizing files by matter and client automatically
> → Exporting research into formats they can file with the court
>
> We have the AI. The research engine works great. But the workflow around it isn't where it needs to be yet. And lawyers won't pay for a tool that creates more work than it saves, no matter how smart the AI is.
>
> So we're in beta. Real attorneys are testing it and telling us exactly what's missing. Every week the product gets closer to launch.
>
> We'll charge when we've earned the right to.

**Template lessons**: Quote a question you keep getting. Distinguish your space from the default playbook. Use a specific contrast ("e-commerce costs a return, legal brief costs a career"). Commit to your standards. End with quiet conviction.

### Pillar C template — Westlaw monopoly (4,479 impressions)

> Westlaw hasn't meaningfully innovated in 20 years.
>
> They don't have to. When you own the data, you don't need a good product.
>
> Think about it. Attorneys pay $200-400/seat/month for what is essentially a keyword search engine with a massive database behind it. The UI looks like it was built in 2008. Because it was.
>
> They added "AI" features recently. You know what that means? A chatbot bolted onto the same search bar. Still can't search your own firm's documents. Still can't cross-reference your case files with public law in one query.
>
> Why would they change? They have the data monopoly. Where else are you going to go?
>
> That's the question I asked myself when I started building.
>
> Turns out, the law is public. Case law is public. Statutes are public. You don't need to pay a gatekeeper $400/month for access to information that belongs to everyone.
>
> You just need someone to build a better way to search it.

**Template lessons**: Punchy contrarian opener. Concrete pricing critique. Identify the moat ("data monopoly"). Reframe the moat as a flaw ("the law is public"). End with the simple alternative.

### Rebrand announcement template — caseread.ai

> Lawless.ai is now Caseread.ai
>
> The old name was fun. It was also, on reflection, a little absurd. Selling software called Lawless to attorneys, the people whose entire profession is the law. Cute in a pitch deck. Less cute on a firm's engagement letter AI disclosure. I'll miss it. Not sure anyone else will.
>
> Enough attorneys told us the same thing that we stopped fighting it.
>
> Same team. Same amazing software, just with a name that lawyers can use without a footnote.
>
> Fun while it lasted. Onward.

**Template lessons**: Self-aware. Lets the audience finish the thought. The "footnote" detail lands because it's specific. Doesn't over-explain.

### Beta-tester quote template — Caseread page repost

> One of our beta testers used Caseread to research Utah restitution law for a criminal hearing this week:
>
> "I just used it to research some restitution laws in Utah, and it gave me a very valuable answer that I intend to use in my argument in a restitution hearing in court on a criminal matter. Super cool."
>
> Hours of research, compressed. Exactly what we built it for.
>
> Try it for yourself while it's free.

**Template lessons**: Specific (Utah, restitution, criminal hearing). Uses customer's own words. One-line takeaway. Soft invite, not a hard sell.

### Hallucination Shield announcement (747 impressions)

> Stanford found that Westlaw's AI hallucinates 33% of the time. Lexis+ AI? 17%.
>
> That means 1 in 3 to 1 in 6 citations these tools generate could be completely fake. Made-up cases. Fabricated docket numbers. Fictional judges.
>
> Countless lawyers have already been sanctioned for filing briefs with AI-hallucinated citations.
>
> So I built something called the Hallucination Shield, a free tool that checks if AI-generated legal citations are real.
>
> How it works:
> → Paste any AI-generated legal text
> → Every citation is verified against our database
> → Get a red/green report in seconds
> → Free. No signup. No cost.
>
> I don't care what AI tool you use, ChatGPT, CoCounsel, Lexis, Claude, Copilot. If it generated citations, you should verify them before filing.
>
> Pulled this tool idea right out of the backend for our AI at Caseread.ai. If you want AI research that verifies citations automatically before you ever see them, that's what the full platform does.
>
> But the checker is free. Use it.
>
> Try it: trylawless.com/verify

**Template lessons**: Stanford stat opener. Stakes-stating ("sanctioned"). Concrete how-it-works arrows. Tool-agnostic stance ("I don't care what AI tool you use"). Free-tool-as-funnel.

---

## Tone DOs and DON'Ts derived from these samples

### DO

- Open with a question, observation, stat, or 3-word punch that makes a lawyer pause
- Cite specific cases / doctrines / rules — they signal credibility
- Use → arrow bullets for enumerated points
- Use specific dollar figures and percentages
- Name foils (Westlaw, Lexis+, Harvey, ChatGPT) when relevant
- Use short paragraphs (2-3 sentences max)
- End with implications, not CTAs
- Tie product back at the end as a natural extension, not a pitch
- Sound like a founder talking to peers, not a marketer

### DON'T

- Open with "I've been thinking..." or "Here's the thing..."
- Use generic "what do you think?" closers
- Stack hashtags (max 1-2 trailing, sometimes more, but don't force it)
- Use legalese without translation
- Over-explain — let the reader finish the thought
- Name specific lawyers / firms in fabricated quotes — only use real testimonials with permission OR anonymized patterns

### Brand-string usage

- Use "Caseread.ai" (current public brand)
- "Lawless" / "Lawless.ai" only appears in old posts before 2026-05-08 (do not generate this in new drafts)
- URL: trylawless.com still works (redirect handles the rebrand transition)
- Tag the company page when relevant: Caseread.ai

---

## Curated additions (appended over time)

_New entries added by the screenshot-ingester skill (planned) as Collin curates patterns from his feed. Each entry captures a structural move, not the original poster._
