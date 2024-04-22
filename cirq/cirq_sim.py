import cirq
import cirq_google
import qsimcirq

# Choose a processor ("rainbow" or "weber")
processor_id = "weber"

# Load the median device noise calibration for your selected processor.
cal = cirq_google.engine.load_median_device_calibration(processor_id)

# Create the noise properties object.
noise_props = cirq_google.noise_properties_from_calibration(cal)

# Create a noise model from the noise properties.
noise_model = cirq_google.NoiseModelFromGoogleNoiseProperties(noise_props)

# Prepare a qsim simulator using the noise model.
sim = qsimcirq.QSimSimulator(noise=noise_model)

# Package the simulator and device in an Engine.
# The device object
device = cirq_google.engine.create_device_from_processor_id(processor_id)
# The simulated processor object
sim_processor = cirq_google.engine.SimulatedLocalProcessor(
    processor_id=processor_id,
    sampler=sim,
    device=device,
    calibrations={cal.timestamp // 1000: cal},
)
# The virtual engine
sim_engine = cirq_google.engine.SimulatedLocalEngine([sim_processor])
# print(
#     "Your quantum virtual machine",
#     processor_id,
#     "is ready, here is the qubit grid:",
#     "\n========================\n",
# )
# print(sim_engine.get_processor(processor_id).get_device())
