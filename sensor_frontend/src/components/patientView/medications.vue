<template>
    <h1 class="mt-2 p-2 py-8 text-3xl shadow-xl">
			Fragebögen für patient: <span class="font-bold text-sky-600">{{patient.last_name}}, {{patient.first_name}}</span>
		</h1>
	<div class="mt-8 flex flex-row">
		<div class="hidden shadow-lg basis-1/3 md:inline">
			<ul class="border-r border-slate-500">
				<li>
					<div
							class="p-4"
							@click="toggleST"
							:class="dropdown1 ? 'mb-10 duration-500 ease-in-out' : 'mb-0 duration-500 ease-in-out'"
					>
						<div class="flex flex-row justify-between py-2 relative border-b border-slate-500">
							<div class="mb-2">
							Selbsttändigkeit
						</div>
						<div
								:class="dropdown1 ?
								'transform rotate-90 transition-transform duration-500' :
								'transform rotate-0 transition-transform duration-500'"
						>
							&rsaquo;
						</div>
						</div>
						<ul>
							<li>
								<div
										class="flex flex-col absolute space-y-4 p-2 duration-500 ease-in-out overflow-hidden text-xs"
										:class="dropdown1 ? 'translate-y-0 opacity-100 pointer-events-auto pb-4' : 'translate-y-[-10px] opacity-0 pointer-events-none'"
								>
									<router-link :to="`/patients/${patient_id}/BarthelIndex`">Barthel Index </router-link>
									<router-link to="/">Pflegediagnostik</router-link>
								</div>
							</li>
						</ul>
					</div>
				</li>
				<li>
					<div
							class="p-4"
							@click="toggleLQ"
							:class="dropdown2 ? 'mb-10 duration-500 ease-in-out' : 'mb-0 duration-500 ease-in-out'"
					>
						<div class="flex relative  flex-row justify-between py-2 border-b border-slate-500">
							<div class="mb-2">
							Lebensqualität
						</div>
						<div
								:class="dropdown2 ?
								'transform rotate-90 transition-transform duration-500' :
								'transform rotate-0 transition-transform duration-500'"
						>
							&rsaquo;
						</div>
						</div>
						<ul>
							<li>
								<div
										class="absolute flex flex-col space-y-4 p-2 duration-500 ease-in-out overflow-hidden text-xs"
										:class="dropdown2 ? 'translate-y-0 opacity-100 pointer-events-auto pb-4' : 'translate-y-[-10px] opacity-0 pointer-events-none'"
								>
									<router-link to="/"> PDQ-8 </router-link>
									<router-link to="/">PDQ-39</router-link>
								</div>
							</li>
						</ul>
					</div>
				</li>
				<li>
					<div
							class="p-4"
							@click="toggleWB"
							:class="dropdown3 ? 'mb-14 duration-500 ease-in-out' : 'mb-0 duration-500 ease-in-out'"
					>
						<div class="flex flex-row relative  justify-between py-2 border-b border-slate-500">
							<div class="mb-2">
							subjektives Wohlbefinden
						</div>
						<div
								:class="dropdown3 ?
								'transform rotate-90 transition-transform duration-500' :
								'transform rotate-0 transition-transform duration-500'"
						>
							&rsaquo;
						</div>
						</div>
						<ul>
							<li>
								<div
										class="absolute flex flex-col space-y-4 p-2 duration-500 ease-in-out overflow-hidden text-xs"
										:class="dropdown3 ? 'translate-y-0 opacity-100 pointer-events-auto pb-4' : 'translate-y-[-10px] opacity-0 pointer-events-none'"
								>
									<router-link to="/">WHO-5 </router-link>
									<router-link to="/">BDI-II</router-link>
									<router-link to="/">EQ-5D-5L</router-link>
								</div>
							</li>
						</ul>
					</div>
				</li>
				<li>
					<div
							class="p-4"
							@click="toggleS"
							:class="dropdown4 ? 'mb-32 duration-500 ease-in-out' : 'mb-0 duration-500 ease-in-out'"
					>
						<div class="flex flex-row relative  justify-between py-2 border-b border-slate-500">
							<div class="mb-2">
							Symptome
						</div>
						<div
								:class="dropdown4 ?
								'transform rotate-90 transition-transform duration-500' :
								'transform rotate-0 transition-transform duration-500'"
						>
							&rsaquo;
						</div>
						</div>
						<ul>
							<li>
								<div
										class="absolute flex flex-col space-y-4 p-2 duration-500 ease-in-out overflow-hidden text-xs"
										:class="dropdown4 ? 'translate-y-0 opacity-100 pointer-events-auto pb-4' : 'translate-y-[-10px] opacity-0 pointer-events-none'"
								>
									<router-link to="/">MoCA</router-link>
									<router-link to="/">MDS-UPDRS</router-link>
									<router-link to="/">NMSS</router-link>
									<router-link to="/">motorische Testung (UPDRS-III)</router-link>
									<router-link to="/">Symtomtagebuch</router-link>
								</div>
							</li>
						</ul>
					</div>
				</li>
				<li>
					<div
							class="p-4"
							@click="toggleV"
							:class="dropdown5 ? 'mb-10 duration-500 ease-in-out' : 'mb-0 duration-500 ease-in-out'"
					>
						<div class="flex flex-row justify-between py-2 border-b border-slate-500">
							<div class="mb-2">
							Inanspruchnahme gesundheitlicher Versorgungsleistungen
						</div>
						<div
								:class="dropdown5 ?
								'transform rotate-90 transition-transform duration-500' :
								'transform rotate-0 transition-transform duration-500'"
						>
							&rsaquo;
						</div>
						</div>
						<ul>
							<li>
								<div
										class="absolute flex flex-col space-y-4 p-2 duration-500 ease-in-out overflow-hidden text-xs"
										:class="dropdown5 ? 'translate-y-0 opacity-100 pointer-events-auto pb-4' : 'translate-y-[-10px] opacity-0 pointer-events-none'"
								>
									<router-link to="/">FIMA</router-link>
									<router-link to="/">Krankenkassendaten</router-link>
								</div>
							</li>
						</ul>
					</div>
				</li>
			</ul>
		</div>
		<div class="basis-2/3 flex justify-center items-center h-96 p-2 text-[min(10vw,30px)]">
			Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam autem corporis dolore eius eligendi
			nihil officia pariatur reiciendis tempore veniam. Illum iure maiores tempora vel voluptatibus? Alias architecto
			assumenda commodi, consequuntur cupiditate dolor exercitationem fuga labore perferendis quasi, totam voluptates?
		</div>
	</div>
</template>
<script setup >
import {usePatientStore} from "@/stores/patient";
import {useRoute} from "vue-router";
import {ref} from "vue";


let patient_id = ref(useRoute().params.id)
const dropdown1 = ref(false)
const dropdown2 = ref(false)
const dropdown3 = ref(false)
const dropdown4 = ref(false)
const dropdown5 = ref(false)
const item = ref('')


const patient = usePatientStore().patient

function toggleST() {
	dropdown1.value = !dropdown1.value
}
function toggleLQ() {
	dropdown2.value = !dropdown2.value
}
function toggleWB() {
	dropdown3.value = !dropdown3.value
}
function toggleS() {
	dropdown4.value = !dropdown4.value
}
function toggleV() {
	dropdown5.value = !dropdown5.value
}



</script>