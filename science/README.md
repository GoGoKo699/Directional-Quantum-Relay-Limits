# Scientific account

The question is an optimization over a physical architecture: what can static local one-way relays achieve when their coherent couplings and required dissipation must come from a passive quantum generator? The answer has two parts. In the absence of additional loss, endpoint engineering preserves a constant transfer probability across arbitrarily long paths, but cannot exceed the two-endpoint pulse-matching ceiling. With a local rate cap and unavoidable loss, the optimal accumulated-loss law can be matched exactly.

The argument proceeds through the following connected topics.

1. [Model and operational task](model.md) specifies the Lindblad generator, complete drift, input/reference contract, retained output, and physical rate conventions. This identifies precisely what the word *directional* requires.
2. [Sharp path ceiling](path_ceiling.md) normalizes the passive damping matrix, proves the classical product inequality in a self-contained form, and turns the unique directed path into a positive convolution. The endpoint response then bounds every static design.
3. [Attainable designs](attainable_designs.md) realizes product saturation with local loss operators and matched coherent hopping. A gamma-distributed transit delay gives an explicit endpoint-rate and waiting-time guarantee.
4. [Loss frontier](loss_frontier.md) separates engineered dissipation from unavoidable loss. It proves the finite upper bound, reduces the exact finite optimization to endpoints and time, and matches both the fixed-loss exponential rate and the full weak-loss crossover.
5. [Channel consequences](channel_consequences.md) applies established pure-loss facts to the optimized physical channel. It distinguishes transmissivity, qubit fidelity, ordinary capacity, assisted capacity and elapsed-time throughput.
6. [A passive bypass](bypass.md) computes a three-mode counterexample to any extension of the ceiling to arbitrary forward graphs. This locates the architectural boundary of the proof.
7. [Physical interpretation](physical_interpretation.md) connects the generator to local reservoir engineering and explains why traveling-field scattering, common-waveguide cascades and reciprocal internal nodes are different tasks or architectures.
8. [Finite examples](finite_examples.md) shows how rigorous bounds and explicit designs compare before taking a limit. Its numerical evidence illustrates the proved statements; it does not replace them.

Each proof has one authoritative home in this sequence. The [related-work account](../references/related_work.md) separates inherited ingredients from the path and loss optimization. The [reproduction route](../REPRODUCIBILITY.md) records the numerical inputs, commands and actual scope of verification.

The exact finite optimum for arbitrary positive loss is represented by an endpoint-and-time optimization, rather than a closed formula. Its optimal polynomial prefactor at fixed loss and the optimal transmission of general multipath graphs are not needed for the matched limits established here.
