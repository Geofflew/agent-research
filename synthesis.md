# The agentic close, 2026 to 2036: what we think will happen

*An integrated view of the future, written 24 October 2026*

This report answers one question in plain words. Over the next ten years, how will agents change the work of closing a company's books inside ERP systems and close platforms? It asks which work agents take first and how that work comes to be trusted, inside and outside the company. It asks what the products must hold, and what happens to the people, the buyers, and the money. Every idea we have formed is folded in, including pictures of the future that compete. Where two pictures cannot both be true, we say so and name what would decide between them.

## Contents

1. The short version
2. 2028: what changes first
3. 2031: the shape settles
4. 2036: two worlds that cannot both be true
5. What each person does differently
6. What this means for a close platform vendor
- Appendix: Signposts to watch

## 1. The short version

Agents will prepare most of the close within ten years. The product that results will be shaped less by agent accuracy than by people, outside clocks, and outside records.

### The close becomes a set of rules a person approves

Routine work such as matching, amortization, and recurring accruals will freeze into fixed rules that an agent drafts. The controller approves each rule once, and the auditor tests it once and then watches for changes. Judgment work goes to agents item by item, with a dollar limit and a confidence score deciding what a person still sees. The controller stops approving entries. The controller approves rules, thresholds, model versions, and the default answers agents give to outsiders.

### Reviewers follow the agent, so honesty needs a blind sample

When an agent says it is confident, reviewers wave the item through. When it says it is unsure, they step in. Ordinary review therefore catches only the errors the agent already flagged. The true error rate comes from a small sample that a person prepares from source documents without seeing the agent's answer. That blind sample becomes the company's real measure of agent quality and the place where a junior still learns the work.

### Clocks that belong to someone else set the pace

The model provider retires models on its own schedule, roughly every twelve to sixteen months. The auditor needs a control unchanged for about two years before cutting fees. The lender wants a package thirty days after month end. Some tax authorities treat silence as an answer after a few days. Wherever an outside clock is stricter than the company's own, it decides where the agent acts, where it stops, and when the month ends.

### Outside records decide where agents must stop

A journal in an open period is cheap to undo because the company reverses it itself. A payment, a locked period, or an invoice cleared through a tax authority is final, because an outside party recorded it. Those are the points where an agent needs a hard stop. Where a public register can check the agent's act, the agent can safely do more. Where the tax authority and banks already hold the data, the company starts reconciling to their numbers.

### The first hard limits have nothing to do with accuracy

What an outside agent may write into a ledger is the ERP vendor's commercial choice, and no law forces it open. Agents also read the invoices and emails that carry payment fraud, and nobody can yet block planted instructions reliably. Bank details and payment release will be carved out of every agent's role.

### Trust from outsiders arrives late and through odd doors

Auditors will not rely on the client's agent for judgment work and will run their own agent instead. Two agents agreeing proves little, because language models tend to make the same mistakes. The first outsiders to set rules for agents may be a crime insurer, a tax authority, or a lender.

### The buyer moves up, and the money moves sideways

Seat pricing loses its base when the agent becomes the preparer. Vendors will charge per task a reviewer accepts, which makes the chief financial officer the buyer. At unaudited private companies the accounting firm buys, because it keeps every hour saved on a fixed fee. At an audited mid-sized company the close costs about the same in 2031 as in 2026. Preparer salaries are replaced by blind samples, scarcer reviewers, a higher audit fee, and usage fees.

### People are lost by not hiring rather than by layoffs

Companies will stop hiring the juniors who used to prepare the close. The finance team turns from a pyramid into a diamond. By about 2032 the scarce resource is mid-level people who can judge exceptions. Whether the profession rebuilds that judgment through the blind sample, or runs out of it, is the largest open question for 2036.

## 2. 2028: what changes first

By 2028 agents prepare much of the routine close at companies that adopt them. People still approve most of it, and outsiders still mostly ignore it.

### Agents take the work that ties out first

Reconciliations go first because a balance either ties or it does not. Vendors shipped matching and automatic sign-off first, then exception detection, then drafted explanations of monthly movements. Some teams instead start with whatever eats the most hours. One staffing company built its first agents for accrual preparation and commission checks and halved its close from twenty days to ten.

### The chart of accounts sets how much goes unreviewed

The first reconciliations to go unreviewed are the static, zero-balance, and predictable accounts. Companies' own reconciliation policies already treat these as low risk. A finance director approves each account onto that list. The agent works the list faster but does not make it longer. Published cases put the unreviewed share between a fifth and two-thirds of accounts, set by each chart of accounts rather than the tool.

### Judgment work passes a dollar limit and a confidence limit

Exceptions spread item by item, the way autonomous medical coding spread through hospitals. The pace is set by the quality of the data feeding the agent, not by the model. An item that scores low because a subledger feed is bad should go to whoever owns that feed. Unlike a medical code, a close error matters only against materiality, the size at which it would change a reader's view. A confident wrong accrual of $400,000 is the whole risk, while a $40 one costs nothing. The threshold is therefore set in dollars as well as confidence, and anything touching a loan covenant goes to a person.

### Informal preferences need testable controls

As a design hypothesis, a preference inferred from one approval should become an explicit rule with visible fields or remain under a sampled threshold. An instruction to treat similar items alike does not, by itself, establish either a stable test baseline or an independent outcome sample. When a rule is edited, the platform re-runs every match under it. The preparer who signed that account reopens the matches that moved and signs again before lock.

### The controller approves rules, thresholds, and model versions

The controller's queue holds proposed rules with their scope and test cases. It holds threshold changes showing which items would move, and switches of a task type to automatic posting. Each change restarts the evidence the auditor relies on. Before lock the controller works down the agent's open-period entries and reverses the ones that looped or misposted. The kill switch for ordinary journals is the period status the controller already holds.

### The reviewer checks a cited policy clause

Agents will cite a versioned policy clause for each treatment, such as a rule to accrue unbilled services above $10,000. The reviewer checks whether the item fits the clause instead of rebuilding the answer. Editing the clause re-runs every open proposal under it. Whoever holds the library of clauses holds the boundary between the ledger and the close platform.

### The preparer's day becomes chasing, sampling, and answering

Shipped agents stop and wait for a finance reviewer when they cannot finish an item. None asks anyone outside finance. The preparer therefore becomes the person who chases receipts, budget owners, and unposted invoices from other departments. Each month the preparer also works a short list of items the agent marked confident. The preparer builds each one from the inputs and only then sees the agent's answer. About sixty items per task type a year is enough to show an agent is clean.

### When agents ask, they should not suggest the answer

The one shipped loop that asks outside finance shows a budget owner an estimate to approve. An approved number is an anchored answer, and auditors treat a person's word alone as weak evidence. Agents should ask the way hospital coders must query doctors. They show the purchase order, receipts, and last period's charge, and offer "I don't know" as an answer.

### The checklist survives with agents signing lines

Agents will tick the preparer's lines on the close checklist and attach their output. The reviewer opens the attachment instead of trusting the tick, and sign-offs with nothing attached are blocked. An agent that finishes early still waits, because task managers open a task only when its predecessor closes.

### Every agent gets a named owner who signs for it

A public company's chief executive and finance chief rely each quarter on sub-certifications from eleven to twenty people below them. When an agent prepared an area, the bottom signer is gone. The staff accountant who signed for cash and accruals now signs as the agent's owner. That person certifies the agent's settings, open exceptions, and sampled error rate rather than the numbers.

### The model changes on the provider's clock

One widely used model retires on 14 January 2027, in the middle of calendar-year audit fieldwork. Every retirement is a software change to an automated control at every customer in the same week. The controller cannot approve a migration from a release note. The preparers work a blind sample before and after the switch, and the controller signs the switch as a control change.

### Controls split into frozen-model judgments and model-free rules

Auditors cut effort only after a clean prior-year opinion on an unchanged control, which takes about two years. Hosted models live twelve to sixteen months. At vendor selection the controller sorts every agent-run control into two kinds. Item-by-item judgments run on a frozen model the vendor hosts. Rules are drafted by any model and then run without one. One cloud service withdraws idle legacy models after fifteen days, so someone keeps the quarter-end model running between closes.

### The auditor answers with its own agent and more testing

The auditor first discounts agent-prepared work and tests more, so audit cost rises before it falls. Auditors then run their own agents over whole populations, as one large firm already does across 1.4 trillion journal lines a year. Every exception the client's agent flags becomes something the auditor must chase. The controller clears flagged exceptions weekly before fieldwork, then reconciles the two exception lists. The preparer ties the auditor's extract back to ledger totals, because no agent proves a population is complete.

### Agreement between two agents proves very little

Language models from different providers tend to make the same mistakes. One study found models agree about sixty percent of the time when both are wrong. The auditor therefore samples entries both agents agree on, not only the disputed ones. At planning the auditor asks which model ran each month, which the controller can answer only from a kept log. The first fee cut cannot appear before the 2027 audit, and a retirement between audits pushes it out a year.

### Bank details and payment release stay with people

Payment fraud hit about three in four US organizations in 2025, and a payables agent reads exactly the messages that carry it. Agents will be set up as their human role minus bank fields and payment release. When the agent finds a new bank account on an invoice, it sends the supplier to the vendor portal. The payables clerk keeps the callback to a number already on file. Crime insurance pays a fraud loss only after a logged employee callback, which gives the clerk an insurance reason too.

### Register countries let the agent do more

Poland publishes every pair of tax number and bank account each day. A buyer who pays an unlisted account shares liability for the supplier's VAT. There a payables agent can enter a new supplier account itself once the register matches. The clerk's callback queue shrinks to the accounts the register rejects, mostly foreign suppliers.

### In clearance countries, issuing an invoice is a hard stop

From September 2026 in France, an issued e-invoice cannot be edited and is corrected only by a new invoice the customer and authority both see. The French billing clerk starts the day with agent-drafted invoices held for checking. The controller decides which invoice types the agent may send alone. Italy has cleared every invoice since 2019 without requiring it, and France's first platforms send automatically.

### Where silence is an answer, waiting is a decision

In Mexico a buyer must accept or reject a supplier's request to cancel an invoice within three business days, or it is accepted. Chile treats unchallenged invoices as accepted after eight days, and Colombia after three business days. An agent that waits for a reviewer has already decided. Its limit must be a deadline it escalates before. The Mexican payables clerk works a short daily queue of requests the agent did not decide. The controller sets the default to rejection for invoices already paid.

### The lender wants a package on time, not a fast close

The median company already closes a month in about six and a half days, weeks inside its filing deadline. US regulators proposed in May 2026 to let companies report twice a year. Speed for public reporting is therefore worth little. The binding clock is the lender's, typically monthly statements within thirty days and quarterly within forty-five. Controllers plan around those dates, and finance chiefs judge agents on cost per close and on-time packages.

### The lender's analyst reads clauses, not entries

In a leveraged borrower the room to move a covenant sits in negotiated add-backs to earnings, not in the bookkeeping. Add-backs appear in up to half of deals, and a central bank study links them to more defaults. The agent posts routine entries and may compute but never propose an add-back. A person approves each add-back against the loan clause that allows it. The analyst covering twenty to twenty-five borrowers checks the cited clauses instead of writing back for detail.

### Unaudited private companies get exception-only review first

Almost two-thirds of medium-to-larger private companies have no audit, only a lender's review, often by an accounting firm on a fixed fee. Only one in ten such firms still bills mainly by the hour, against more than half in 2018. These firms keep every saving their agents produce, so they reach exception-only review first. Independence rules make the owner's monthly acceptance of the agent's decisions the real control. If the owner skips that sitting, the lender gets a report saying the firm is not independent.

### In India the close stops feeding the loan

Indian public-sector banks now lend to small businesses straight from tax returns and bank data, deciding within a day. The close is no longer an input to the loan. The accountant's month ends when the agent's list of invoices that differ from the tax return is cleared. That must happen before the return locks on the 20th. The person who signs the return is the last check the lender relies on.

### Lenders elsewhere add a login but keep the audit

A lender that can log into a borrower's books still asks for the audit. Audited private companies borrow at about three-quarters of a point less. The lender pays for someone outside testing the estimates, which a login shows but does not check.

## 3. 2031: the shape settles

By 2031 the near-term limits have hardened into market structure. Several pictures of that year compete. They disagree on who runs the small company's close, which outsider first accepts agent work, and where the slow step sits.

### The accounting firm runs the small company's close

A $20 million distributor has no bookkeeper, no close software, and no controller. Its accounting firm's agents post every night, and one accountant works its exceptions alongside about sixty other clients. On the fifth business day the owner spends forty minutes in a recorded sitting accepting or returning each decision. Firms reprice or drop clients whose messy data feeds produce too many exceptions. Growing companies put off their first audit, because the auditor's own agent erases the saving.

### Or the ERP vendor's own agents run it

In this picture ERP vendors charge for every write an outside agent makes. ERPs already cap outside calls, so only a price per write is new. A general-purpose agent working item by item makes far more writes than the ERP's own agent running rules inside the ledger. The outside agent close becomes uneconomic. The accounting firm absorbs any such charge inside its fixed fee, which is why these two pictures pull apart.

### Or a general-purpose agent does it

Here a small company's accountant uses the same general-purpose agent the rest of the company uses. It reaches the ledger, bank, billing, and spend tools through their published connections. It loads procedure skills bought from former close software companies through the model provider's marketplace. This picture needs ledgers to stay open to outside writes. Even then a model provider's own connector may withhold posting, as one already does on QuickBooks.

### Or a private equity sponsor buys one close for forty companies

A sponsor puts every portfolio company on one outsourced finance provider whose agents post all their entries. The sponsor's portfolio finance lead accepts each company's decisions in one weekly queue. Each company keeps only a finance chief and the people who answer the agents. At the 2031 refinancings lenders demand a reviewer that neither the sponsor nor the provider controls.

### Or a model provider owns the firm that keeps the books

Private equity bought into large US accounting firms from 2021 to 2024 by splitting each into a partner-owned audit firm and an investor-owned advisory firm. In this picture a model provider buys the advisory half and keeps thousands of small companies' books on its own models. It pins its clients' model through each audit year while moving everyone else on its retirement schedule. This picture and the sponsor picture can both come true.

### The independence line may move from the engagement to the owner

In a darker version, a platform owned by private equity runs agent closes in one company and reviews in a sister company. A client's close misreads a customer prepayment as revenue for six quarters, and the review relied on an acceptance rate near one hundred percent. The client breaches its covenants and the lender sues. Regulators then treat common ownership of the two businesses as a conflict for shared clients.

### Tax authorities may draft the smallest companies' books

Clearance-country authorities already hold both sides of most invoices, and Chile and Italy already build companies' purchase and sales registers from them. One picture extends that to a monthly draft ledger built from invoices, payroll filings, and bank data. The company's agent disputes the draft, and the owner validates it each quarter. The bottom tier of outsourced bookkeeping disappears.

### What decides who runs the small company's close

Prices per outside write at the 2027 to 2029 ERP renewals would favour the ERP. Rising fixed-fee share and clients per accountant in the 2028 and 2030 practice surveys would favour the firm. A portfolio-wide close contract by 2029 would bring the sponsor picture. A model provider owning an advisory arm by 2030 would bring the provider picture. We expect the accounting firm to win the smallest companies and the ERP to win most of the mid-market.

### The first outsider to accept agent work prices a different risk

Several outside parties compete to accept agent work first. The crime insurer prices manipulation. The close vendor's attested report prices error. The lender prices the reliability of the record. The tax authority prices the legality of each act an agent signs.

### The crime insurer may license the payables agent

Fraud cover pays only if an employee verified a changed bank instruction by a logged callback. An agent changing a supplier account would therefore void the cover. At the 2027 and 2028 renewals carriers must exclude agents or rewrite the clause. In this picture they admit an agent that holds a yearly certification and passes a bank name match. The controller learns what the payables agent may do at the insurance renewal, not at audit planning.

### Or a fraud wave moves payee control to the bank

A harder version starts with a 2029 campaign of forged supplier invoices carrying hidden instructions. One widely used payables agent reads them as bank changes, and hundreds of companies lose money in one month. Insurers exclude agent payments to unverified payees. Banks then pay agent transfers only to payees registered in advance through a channel no agent touches.

### Or the close vendor becomes the audited party

Here auditors rely on the close vendor's attested error rate per task type, as they rely on a payroll processor today. The vendor draws one blind sample across all its customers, which no single company could afford. A customer that changes a setting loses coverage for that task type.

### Or the auditor re-prepares the whole routine close

The opposite picture has the audit firm's agent re-prepare every reconciliation and accrual blind and compare. Of 1.4 million entries, perhaps three hundred differ. The audit senior sorts them into policy differences, missing documents, and real errors before lunch. Re-preparation costs compute rather than staff hours, so routine fees fall even without a clean control history.

### Or the lender reads the authority's record directly

In a clearance country a mid-market lender pulls cleared invoices from the tax authority and payments from the banks each week. It computes revenue, margin, and cash itself. A supplier's duplicate invoice then sits in the borrower's covenant figure until the supplier corrects it. Credit agreements add a cure period for disputed cleared invoices.

### Or the lender pays for the borrower's close

A direct lender with hundreds of borrowers finds late, inconsistent packages expensive. In this picture it pays accounting firms to run every borrower's agent close and builds the cost into the loan margin. The lender becomes the buyer of the close. Because it pays, it cannot treat the firm's review as independent and keeps its own monitoring.

### Or a regulator writes the first agent rules

In a clearance country an agent's acceptance or rejection of an invoice is already a legal act. One picture has the French tax authority extend its accreditation of invoicing platforms to the agents on them. The agent reading invoices must be separate from any agent touching payment details, and every status carries the agent's identity. Another has the EU list financial reporting agents as high-risk AI after the Commission's August 2028 report. The first outside check then becomes a conformity assessment of the vendor, repeated whenever the model changes.

### What decides the first outsider

A crime insurance application asking about agents changing bank details by the 2028 renewals would favour the insurer. A vendor controls report covering agent error rates for 2028 or 2029 would favour the vendor. A French or Polish lender monitoring from e-invoice data within a year of September 2027 would favour the lender. We think the insurer moves first on payments and the tax authority first on invoices. The auditor comes last.

### The critical path runs through people outside finance

Once agents sign most checklist lines, finance stops being the slow part. On day two of a quarter-end close, a $200 million distributor's orchestrator shows 412 tasks, with 371 signed by agents. The path to the lender's certificate runs through nine people outside finance. They include a sales director checking side letters and a lawyer pricing a lawsuit. When the lawyer answers, the orchestrator re-dates every dependent task, and managers outside finance carry close deadlines in their objectives. The controller manages the company's answers rather than its accounting.

### Verification eats the savings at audited companies

A worked budget for a $500 million audited company shows the same total in 2026 and 2031, about $1.5 million. Four of six preparer seats go unfilled. Two staff accountants spend most of their year on the blind sample. Reviewers and the audit fee cost more, and usage fees replace the licence.

### Cheap detail and model failures reshape the rules

When agents classify every entry against frozen rules, detailed disclosure becomes cheap. One picture has standard setters stop accepting preparers' cost objections and ask for more detail, so the public close trades speed for depth. A mid-year model update that misstates one accrual at hundreds of audited customers in 2030 would pin every close agent to one model per fiscal year. A provider outage stopping thousands of year-end closes in January 2032 would bring a yearly close drill without agents, which keeps preparers employed.

## 4. 2036: two worlds that cannot both be true

Ten years out the pictures split into pairs that exclude each other. Each pair turns on one question we cannot yet answer. This chapter sets out each pair and what would decide it.

### The ledger absorbs the close

In one world the month-end close stops existing as an event or a product. Ledgers own billing, spend, payroll feeds, and bank connections. Their own agents post, match, accrue, and amortize as transactions happen. Month end becomes a lock after the controller clears a short list of unsettled items.

### Or the close layer owns the ledger

In the other world the system a finance chief calls "finance" is not the ERP. It is a control layer holding the company's policies, each agent's limits, and the credentials agents use with banks, tax authorities, and lenders. Several ERPs sit underneath as interchangeable posting engines. The information officer buys the ERP as infrastructure, and the finance chief buys the layer per governed agent. Today's treasury payment hub, with approval rules across several ERPs, is its template.

### What decides between them

The question is where a finance limit can be written. A limit such as "accruals to these accounts, under this amount, in an open period" needs amounts, periods, and policy in one place. A company on one ERP can write it inside the ledger. A company on several can write it only above them. ERPs shipping agent identities scoped by amount and period before 2030 would favour the ledger. A close vendor holding agent identities that a bank accepts by 2029 would favour the layer.

### Lenders drop the audit for ledger access

In one world US banks replace the loan size at which they demand an audit with a demand for ledger access. They also ask for the accounting firm's measured error rate by task type. Reviews get cheaper while audits do not, because auditors still run their own agents. Most mid-market borrowers take the alternative. The private-company audit shrinks to a product for selling a company or raising equity.

### Or verifiability is priced into the loan

A softer version keeps the audit optional but prices verifiability, and a bolder one has statement insurance replacing the audit. A company with a measured error rate and revenue reconciled to bank receipts borrows at a lower spread. Indian small-business borrowers with more verifiable payments already pay less and default less.

### Or the audit survives because it tests the estimates

In the other world the audit holds. What it buys a lender is an outside test of accruals and estimates. A live login shows what an agent posted but not whether the judgments behind it are sound. Reviews already match audits on measured quality and still do not earn the lower rate. This is the world we expect. A filed loan accepting system access in place of an audit before 2030 would prove us wrong.

### The audit committee runs its own agent

At listed companies one picture has the audit committee running its own agent over the ledger through internal audit. That agent reports to the directors, not to management. Each night it reads every journal and every management agent's settings. Each quarter it re-prepares a blind sample and lists the entries it would have treated differently. The external auditor tests the board's agent and runs its own only over high-judgment areas. A management change to an agent's settings reaches the committee chair the next morning.

### Or the auditor's agent and the client's agent negotiate

The rival keeps the auditor's own agent at the centre. In its sharpest form fieldwork becomes a signed exchange between the two agents, where silence accepts the auditor's proposed treatment. The controller's audit work becomes deciding which answers to defend before the clock runs out. One picture had regulators require different model families on each side. Correlated errors across providers cut against it, because only a person working blind gives an independent check.

### The blind sample becomes the apprenticeship

In one world a first-year accountant's job is preparing the company's blind sample. The junior opens seven items drawn overnight from finished agent work and prepares each without the agent's answer. At lunch the comparison unlocks, and the manager signs the morning as supervised experience. Licensing boards count that queue as qualifying work.

### Or juniors are hired to attack the agents

A variant hires first-year accountants to attack the company's finance agents. Insurers and auditors require adversarial testing for the yearly agent certifications they accept. Outside testers know models but not a distributor's suppliers and rebate terms. The junior builds forged invoices and fake "new controller" emails from real suppliers and records what got through.

### Or nobody is left who can judge

In the opposite world companies stopped hiring juniors and kept no training queue. By 2033 manager seats are filled by people who only ever reviewed agent output. Auditors report material weaknesses because reviewers cannot recompute the agent's figures. Boards buy judgment at any price, hiring back retirees and former audit managers. A related world has small companies renting a controller's signature, one licensed professional signing for twenty or thirty companies' agents.

### What decides the profession's future

Large UK audit firms are still raising graduate intake, so the shortage is a company problem for now. The first two-year US licensing cohorts finish in Texas from August 2028 and California from January 2029. A state board ruling that blind preparation counts as experience would favour the apprenticeship. Rising material weaknesses for too few accounting staff in the 2027 to 2030 annual reports would favour the profession running dry.

### Standard setters ship the rule as code

In one world standard setters publish each new standard's rules as an executable rule set with test cases. Every close vendor loads the same set in a parallel quarter, and the controller signs the switch on the effective date. A company whose facts differ records a departure with its reasons. The auditor reviews the departures list rather than the whole class. Inconsistent agent application of the 2027 presentation standard is what starts it.

### Or the law reserves judgments to a licensed person

The rival world draws the agent's edge by statute. State accountancy laws reserve going concern, impairment, inventory obsolescence, and revenue estimates to a licensed person the company employs. The agent prepares data and a draft, and that person signs the judgment. A third world leaves estimates with people because auditing an agent's estimate costs more than preparing it. There the audited close is half automated and the unaudited close fully automated.

### Companies' agents deal with each other directly

Several pictures put agents on both sides of a deal. A supplier's agent and a customer's agent agree each sale on one cleared record that both ledgers post. The receivable and the payable become the same fact. The three-way match, the supplier statement reconciliation, and the receivables confirmation disappear for trade inside the EU. Balance confirmations run system to system under defaults the controller sets in advance.

### The payment date is priced invoice by invoice

Once an issued invoice cannot be edited, the payment date is the one term left to bargain. A Dutch distributor's agent receives 3,400 cleared supplier invoices in a week. For each, the supplier's agent posts a price for payment today, in ten days, and at term. The distributor's agent accepts where the discount beats its cost of cash, within the controller's daily limit. Small suppliers get cash the day they clear an invoice, and banks lose that short-term lending.

### The bank keeps the small company's books

In another picture small companies stop buying a ledger. The bank holding the operating account already sees the payments and receives the e-invoices. Its agent drafts the accruals, depreciation, and deferred revenue that remain. One UK bank already gives bookkeeping away with the account. The bank cannot rely on books it prepared, so it pays an accounting firm to review them. That firm can review because it no longer posts.

### What decides who holds the small company's books

The bank picture needs a large bank offering an agent that posts month-end entries for business customers by 2029. The payment-date picture needs a platform offering per-invoice agent pricing on cleared invoices by 2031. Europe's instant payments since October 2025 and cross-border e-invoicing from July 2030 are the rails both need. If small companies still buy accounting software separately in 2032, the bank picture fails.

### The portfolio close is sold at exit

A last picture follows the sponsor's single close to the sale of a portfolio company. The buyer finds no finance function to take over. It receives the agent register, settings, named owners, and five years of error rates in the data room. It cuts the price where a model retirement restarted a task type's error history.

## 5. What each person does differently

Every idea above lands on someone's working day. This chapter gathers the changes by role.

### The preparer

The preparer stops building routine reconciliations and works what the agent could not finish. Much of the day goes to chasing receipts, budget owners, and unposted invoices from other departments. Each month the preparer works the blind sample from inputs before seeing the agent's answer. When a matching rule changes, the preparer reopens the matches that moved and signs again. In clearance countries each close starts from the differences between the ledger and the authority's register.

### The controller

The controller stops approving entries and approves the settings agents run on. These are rules, thresholds, task types switched to automatic posting, model migrations, and default answers to outsiders. Before lock the controller reverses the agent's looped entries and takes it out of the period. The controller reads the blind disagreement rate and keeps the log of which model ran each month.

### The reviewer or manager

The mechanical check of agent output disappears, because the agent's computed checks tie out every item. The manager's review stays for new treatments, estimates, and policy citations. That queue peaks in the third month of each quarter, when reconciliation tools hand certification back to a person. The manager supervises juniors by comparing their blind figures with the agent's.

### The external auditor

The auditor first discounts agent work and tests more, then runs its own agent over whole populations. The auditor asks at planning which model ran each month and re-plans after each retirement. Entries both agents agree on get sampled, because agreement is not evidence. The first fee cut comes no earlier than the third audited year on an unchanged model.

### The lender's analyst

The analyst covers twenty to twenty-five borrowers a month and recomputes each covenant. With clause-linked add-back schedules, the analyst checks clauses instead of asking for detail. In clearance countries the analyst reads the tax authority's record and handles a queue of disputed invoices. The analyst still asks for the audit unless filed agreements start accepting a measured error rate.

### The accounting firm owner

The owner keeps every hour the agents save, because the firm bills a fixed fee. Its accountants work one queue across sixty clients. The owner must make sure each client's owner attends the monthly acceptance sitting, or the review report fails. A firm that designs and runs a client's agent rules is running the client's systems, so it must choose between running closes and giving reviews.

### The close platform vendor

Seat revenue shrinks as the agent becomes the preparer. The vendor moves to pricing per accepted task and must keep the blind sample outside the bill. It pins models per customer fiscal year and may host frozen models itself. It needs to hold policy clauses, limits across ERPs, agent identities, and a register of named owners.

### The ERP vendor

The ERP vendor decides which write actions outside agents get, and no law forces it to open them. Once its own close agent ships, it can narrow or charge for outside writes. Its data design decides how safely bank details stay out of an agent's reach. Large SAP customers adopt close agents during their 2027 to 2033 migrations. The ERP vendor either absorbs the close or becomes a posting engine under someone else's control layer.

### The buyer

The buyer moves from the controller to the finance chief once vendors price per accepted task. At unaudited companies the accounting firm buys, and in some markets the lender, sponsor, or bank buys instead. The finance chief reads an ERP's agent tool list as a contract term when choosing a ledger. The finance chief books no audit saving before the third audited year and pays for measured accuracy rather than days saved.

## 6. What this means for a close platform vendor

The ideas in this report point to a clear product agenda for a close platform. Build the record of rules, thresholds, and policy clauses that agents read and controllers approve. Show the scope of every "apply to similar items" as fields the controller can freeze, test, and version. Ship a blind sample drawn from the items the agent marked confident, with the agent's answer hidden until the person commits. Keep a log of which model ran each task each month, and pin models through each customer's fiscal year. Write limits in amounts, accounts, and periods above every ledger the customer runs, because ERP permissions cannot express them. Give agents a way to ask people outside finance open questions, and re-plan the close when answers come late.

Stop building screens whose only job is approving one agent answer at a time. Stop selling days-to-close as the headline benefit, because nobody outside the company pays for it. Stop treating reviewer acceptance as proof of accuracy, in the product or on the invoice.

Sell per accepted task to the finance chief of an audited company, with sampled items never billed. Sell multi-client queues and recorded owner sittings to accounting firms, the first buyers able to bank the saving. Sell clause-linked add-back schedules and on-time packages to borrowers and their lenders. Sell a register of agents, owners, and settings to public companies facing quarterly certification. Commission a controls report on your own agents, because the vendor auditors can rely on wins the mid-market.

## Appendix: Signposts to watch

- On 14 January 2027 one major provider retires a widely used model inside calendar-2026 audit fieldwork, the first test of model change as control change.
- From 1 January 2027 Poland drops its income tax penalty for paying unlisted bank accounts but keeps the buyer liable for the supplier's VAT.
- By March 2027 Microsoft plans ERP restrictions that apply only when a user acts through an agent.
- The new international presentation standard takes effect for 2027, the first major standard applied with close agents in use.
- The 2027 audit is the first in which a fee cut from agent monitoring could appear, disclosed in 2028 proxy statements.
- In September 2027 France's e-invoicing mandate reaches smaller companies, and the default for agent-drafted invoices will show whether holding them becomes normal.
- At the 2027 and 2028 renewals, crime insurers will either write agents into the callback clause or exclude them.
- At the 2027 to 2029 ERP renewals, a price per outside agent write would show ledger vendors closing the door.
- In August 2028 the European Commission reports on new high-risk areas under the AI Act, where financial reporting could appear.
- From August 2028 in Texas and January 2029 in California, the first two-year licensing cohorts finish and test what counts as supervised experience.
- By 2028 one large audit firm expects its platform to run every audit activity end to end.
- Between 2028 and 2031 private equity owners sell the advisory halves of large accounting firms, revealing who will keep small companies' books.
- In 2030 extended maintenance on SAP's old ERP ends, forcing the largest wave of replacements that will settle where close limits live.
- From 1 July 2030 cross-border invoices inside the EU are reported to tax authorities, completing the outside record lenders and agents read.
- The 2031 refinancing vintage of private credit will show whether lenders accept ledger access and error rates in place of the audit.
